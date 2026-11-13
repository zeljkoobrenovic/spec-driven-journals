#!/usr/bin/env bash
# Run the sharpen-post skill through the claude CLI on every post of a journal,
# in config.yaml order, one headless session per post.
#
# Usage:
#   .claude/skills/sharpen-post/scripts/sharpen_journal.sh [options] [journal]
#
#   journal          journal folder under _journals/ (default: listing-systems-architecture)
#   -j N             run N posts in parallel (default 1; builds may collide above ~3)
#   -m MODEL         model passed to claude --model (default: the CLI default)
#   -o SLUG[,SLUG]   only these post folders (e.g. 46-case-adevinta)
#   -s SLUG[,SLUG]   skip these post folders (default: bibliography,glossary)
#   -f               re-run posts whose spec.md already logs a "Sharpening pass"
#   -n               dry run: list the posts that would run
#   -c               after the run, a read-only claude session checks headings
#                    and terms across chapters (report only, no edits)
#   -C               run only that check, without sharpening (-o sets its scope)
#   -A               check the whole book; by default the check reports only on
#                    this run's posts and their neighbours in config.yaml order
#   -t MIN           time limit per post session (default 15 minutes)
#   -T MIN           time limit for the -c check session (default 20 minutes)
#
# Logs go to _temp/sharpen-post/<journal>/<folder>.log. Every run also writes
# results.md there (per post: words before -> after against HEAD, headings
# changed, fact-check result, then each session's REPORT block: title
# suggestion, deleted claims, questions for the author), outlines.md (all chapters' headings in book
# order) and, with -c, consistency.md. A session over its time limit is
# stopped and recorded as "timeout". Nothing is committed: review with git diff.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
cd "$ROOT"
SKEL=".claude/skills/sharpen-post/scripts/skeleton.py"
FACT=".claude/skills/sharpen-post/scripts/factcheck.py"

JOBS=1 MODEL="" ONLY="" SKIP="bibliography,glossary" FORCE=0 DRY=0 CHECK=0 CHECK_ONLY=0 WHOLE=0 LIMIT=15 CHECK_LIMIT=20
while getopts "j:m:o:s:t:T:fncCAh" opt; do
  case "$opt" in
    j) JOBS="$OPTARG" ;;
    m) MODEL="$OPTARG" ;;
    o) ONLY="$OPTARG" ;;
    s) SKIP="$OPTARG" ;;
    f) FORCE=1 ;;
    n) DRY=1 ;;
    c) CHECK=1 ;;
    C) CHECK=1; CHECK_ONLY=1 ;;
    A) WHOLE=1 ;;
    t) LIMIT="$OPTARG" ;;
    T) CHECK_LIMIT="$OPTARG" ;;
    *) sed -n '2,28p' "$0"; exit 0 ;;
  esac
done
shift $((OPTIND - 1))
JOURNAL="${1:-listing-systems-architecture}"
CONFIG="_journals/$JOURNAL/config.yaml"
[[ -f "$CONFIG" ]] || { echo "no $CONFIG" >&2; exit 1; }
command -v claude >/dev/null || { echo "claude CLI not found" >&2; exit 1; }

LOGDIR="_temp/sharpen-post/$JOURNAL"
mkdir -p "$LOGDIR"

in_list() { [[ ",$2," == *",$1,"* ]]; }

# Post folders in config.yaml order.
all_posts=()
while IFS= read -r folder; do all_posts+=("$folder"); done \
  < <(sed -nE 's#^[[:space:]]*-[[:space:]]+([^/[:space:]]+)/index\.md[[:space:]]*$#\1#p' "$CONFIG")

posts=() selected=()
for folder in "${all_posts[@]}"; do
  [[ -n "$ONLY" ]] && ! in_list "$folder" "$ONLY" && continue
  in_list "$folder" "$SKIP" && continue
  selected+=("$folder")
  [[ $CHECK_ONLY -eq 1 ]] && continue
  spec="_journals/$JOURNAL/posts/$folder/spec.md"
  if [[ $FORCE -eq 0 && -f "$spec" ]] && grep -q "Sharpening pass" "$spec"; then
    echo "[done] $folder (already sharpened; -f to redo)"
    continue
  fi
  posts+=("$folder")
done

# The check's scope: the selected posts and their neighbours, or the whole book.
scope=()
if [[ $WHOLE -eq 0 && ( -n "$ONLY" || $CHECK_ONLY -eq 0 ) ]]; then
  for i in "${!all_posts[@]}"; do
    for d in -1 0 1; do
      j=$((i + d)); (( j < 0 || j >= ${#all_posts[@]} )) && continue
      for s in ${selected[@]+"${selected[@]}"}; do
        if [[ "${all_posts[$j]}" == "$s" ]]; then scope+=("${all_posts[$i]}"); break 2; fi
      done
    done
  done
fi

if [[ $CHECK_ONLY -eq 1 ]]; then
  echo "Check only; scope: ${scope[*]:-whole book}"
  [[ $DRY -eq 1 ]] && exit 0
else
  echo "${#posts[@]} post(s) to sharpen in $JOURNAL, $JOBS at a time"
  [[ $DRY -eq 1 ]] && { printf "  %s\n" ${posts[@]+"${posts[@]}"}; echo "Check scope: ${scope[*]:-whole book}"; exit 0; }
fi

ALLOWED=(
  Read Edit Write Grep Glob
  "Bash(python3:*)" "Bash(python3.11:*)"
  "Bash(git diff:*)" "Bash(git show:*)" "Bash(git status:*)"
  "Bash(grep:*)" "Bash(sed -n:*)" "Bash(wc:*)" "Bash(head:*)" "Bash(tail:*)" "Bash(ls:*)"
)

# Run a command with a time limit (macOS has no timeout(1)). Stdin comes from $1,
# stdout and stderr go to $2. Returns the command's status, or 124 on timeout.
run_limited() {
  local input="$1" output="$2" minutes="$3"; shift 3
  local rcfile="$output.rc"
  rm -f "$rcfile"
  # A detached subshell in its own process group records the exit status; on
  # timeout the whole group (claude and anything it started) is killed quietly.
  set -m
  ( "$@" <"$input" >"$output" 2>&1; echo $? >"$rcfile" ) 2>/dev/null &
  local pid=$! waited=0
  set +m
  disown "$pid" 2>/dev/null || true
  while kill -0 "$pid" 2>/dev/null; do
    # SHARPEN_LIMIT_SECONDS overrides the limit, for testing the timeout path.
    if (( waited >= ${SHARPEN_LIMIT_SECONDS:-$((minutes * 60))} )); then
      kill -TERM -- "-$pid" 2>/dev/null; sleep 2
      kill -KILL -- "-$pid" 2>/dev/null
      rm -f "$rcfile"
      return 124
    fi
    sleep 5; waited=$((waited + 5))
  done
  local rc
  rc=$(cat "$rcfile" 2>/dev/null || echo 1)
  rm -f "$rcfile"
  return "$rc"
}

STATUS="$LOGDIR/status.txt"
[[ $CHECK_ONLY -eq 0 ]] && : > "$STATUS"

sharpen_one() {
  local folder="$1" file="_journals/$JOURNAL/posts/$1/index.md" log="$LOGDIR/$1.log"
  local start=$SECONDS prompt="$LOGDIR/$1.prompt" rc=0
  echo "[start] $folder"
  # --allowedTools is variadic, so pass it as one comma-separated value and send the prompt on stdin.
  local tools
  tools="$(IFS=,; echo "${ALLOWED[*]}")"
  local args=(-p --permission-mode acceptEdits --no-session-persistence --allowedTools "$tools")
  [[ -n "$MODEL" ]] && args+=(--model "$MODEL")
  printf '%s\n\n%s\n' "/sharpen-post $file" \
    "Run the skill autonomously on this one post: do not ask questions, do not edit other posts, do not commit. Finish with the skill's short report, and end it with this block exactly, one line per field, 'none' when empty:
REPORT
title: <suggested title and why, or none>
deleted claims: <each deleted claim or quote with its reason, separated by '; '>
questions: <questions for the author, separated by '; '>
END REPORT" > "$prompt"
  run_limited "$prompt" "$log" "$LIMIT" claude "${args[@]}" || rc=$?
  rm -f "$prompt"
  local state=ok
  if [[ $rc -eq 124 ]]; then state=timeout; elif [[ $rc -ne 0 ]]; then state=fail; fi
  echo "$folder $state $((SECONDS - start))" >> "$STATUS"
  printf '[%-7s] %s (%ss) — %s\n' "$state" "$folder" "$((SECONDS - start))" "$log"
}

if [[ ${#posts[@]} -eq 0 ]]; then
  :
elif [[ "$JOBS" -le 1 ]]; then
  for folder in "${posts[@]}"; do sharpen_one "$folder"; done
else
  for folder in "${posts[@]}"; do
    while [[ $(jobs -rp | wc -l) -ge $JOBS ]]; do sleep 2; done
    sharpen_one "$folder" &
  done
  wait
fi

if [[ $CHECK_ONLY -eq 0 ]]; then
  echo "Rebuilding to confirm the journal still builds..."
  python3 _wiring/build.py 2>&1 | grep -iE "$JOURNAL|error|Traceback" || true
fi
# Every chapter's outline in one file, so headings and terms can be read side by side.
OUTLINES="$LOGDIR/outlines.md"
{
  echo "# Outlines: $JOURNAL"
  for folder in "${all_posts[@]}"; do
    file="_journals/$JOURNAL/posts/$folder/index.md"
    [[ -f "$file" ]] || continue
    echo; echo "## $folder ($(python3 "$SKEL" "$file" --stats))"
    python3 "$SKEL" "$file" --headings | sed 's/^/    /'
  done
} > "$OUTLINES"
echo "Outlines of all chapters: $OUTLINES"

# Results table for the posts this run touched, measured against HEAD.
if [[ ${#posts[@]} -gt 0 && -s "$STATUS" ]]; then
  RESULTS="$LOGDIR/results.md"
  {
    echo "# Sharpening results: $JOURNAL ($(date '+%Y-%m-%d %H:%M'))"
    echo
    echo "Measured against HEAD; a post with uncommitted changes from before the run counts them too."
    echo
    echo "| Post | Session | Time | Prose words | Headings changed | Fact check |"
    echo "| --- | --- | --- | --- | --- | --- |"
    for folder in "${posts[@]}"; do
      file="_journals/$JOURNAL/posts/$folder/index.md"
      read -r _ state secs < <(grep "^$folder " "$STATUS" || echo "$folder missing 0")
      after=$(python3 "$SKEL" "$file" --stats | sed 's/.*prose_words=//')
      before=$(git show "HEAD:./$file" 2>/dev/null | python3 "$SKEL" /dev/stdin --stats | sed 's/.*prose_words=//')
      headings=$(git diff -U0 -- "$file" | grep -c '^+#' || true)
      lost=$(python3 "$FACT" "$file" | grep -cE '^(LOST|CHANGED|FIGURES|POINTER )' || true)
      [[ "$lost" -eq 0 ]] && check="OK" || check="$lost flagged (see log)"
      echo "| $folder | $state | ${secs}s | ${before:-?} → $after | $headings | $check |"
    done
    echo
    echo "## Session reports"
    for folder in "${posts[@]}"; do
      echo; echo "### $folder"
      block=$(sed -n '/^REPORT[[:space:]]*$/,/^END REPORT/p' "$LOGDIR/$folder.log" 2>/dev/null | sed '1d;$d')
      if [[ -n "$block" ]]; then echo "$block" | sed 's/^/- /'; else echo "- no REPORT block; read $LOGDIR/$folder.log"; fi
    done
  } > "$RESULTS"
  sed -n '5,/^## Session reports/p' "$RESULTS" | sed '$d'
  echo "Results: $RESULTS"
fi

if [[ $CHECK -eq 1 ]]; then
  echo "Checking headings and terms across chapters (read-only, ${CHECK_LIMIT} min limit)..."
  check_args=(-p --no-session-persistence --allowedTools "Read,Grep,Glob")
  [[ -n "$MODEL" ]] && check_args+=(--model "$MODEL")
  DECISIONS="_journals/$JOURNAL/_research/heading-decisions.md"
  prompt="$LOGDIR/consistency.prompt"
  if [[ ${#scope[@]} -gt 0 ]]; then
    scope_note="Report findings only for these chapter folders: $(IFS=,; echo "${scope[*]}"). Read the other outlines only for comparison."
  else
    scope_note="Report findings for every chapter."
  fi
  printf '%s\n' "Read $OUTLINES: the heading outline of every chapter in _journals/$JOURNAL, in book order, after a sharpen-post pass that edited each chapter in isolation. Read _journals/$JOURNAL/README.md and any _research/style-guide.md or glossary post for the book's fixed terms. If $DECISIONS exists, read it: it records heading conventions the author has already decided, including variations that are intentional. Do not report anything it covers; list only new findings. $scope_note Report, without editing anything:
1. the same concept named differently in different chapters' headings (give both wordings, the chapters, and which wording to keep, preferring the glossary's);
2. headings in the same position across parallel pages (part intros, cases, hand-offs) that no longer share a shape;
3. headings that became vague or generic;
4. headings that look renamed but are still cited under the old name elsewhere (grep the posts to confirm);
5. post titles or excerpts whose terms disagree with the glossary, the scenario ledger or the post's own headings.
Group findings by chapter folder, one line each, most important first. Say 'No issues' for a clean category." > "$prompt"
  rc=0
  run_limited "$prompt" "$LOGDIR/consistency.md" "$CHECK_LIMIT" claude "${check_args[@]}" || rc=$?
  rm -f "$prompt"
  if [[ $rc -eq 0 ]]; then echo "Consistency report: $LOGDIR/consistency.md"
  elif [[ $rc -eq 124 ]]; then echo "Consistency check stopped after ${CHECK_LIMIT} min; what it wrote is in $LOGDIR/consistency.md"
  else echo "Consistency check failed; see $LOGDIR/consistency.md"; fi
fi

echo "Done. Review with: git diff --stat -- _journals/$JOURNAL"
