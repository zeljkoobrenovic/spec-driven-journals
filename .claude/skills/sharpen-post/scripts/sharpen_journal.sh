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
#                    and terms across all chapters (report only, no edits)
#
# Logs go to _temp/sharpen-post/<journal>/<folder>.log. Every run also writes
# outlines.md there (all chapters' headings in book order) and, with -c,
# consistency.md. Nothing is committed: review the result with git diff.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
cd "$ROOT"
SKEL=".claude/skills/sharpen-post/scripts/skeleton.py"

JOBS=1 MODEL="" ONLY="" SKIP="bibliography,glossary" FORCE=0 DRY=0 CHECK=0
while getopts "j:m:o:s:fnch" opt; do
  case "$opt" in
    j) JOBS="$OPTARG" ;;
    m) MODEL="$OPTARG" ;;
    o) ONLY="$OPTARG" ;;
    s) SKIP="$OPTARG" ;;
    f) FORCE=1 ;;
    n) DRY=1 ;;
    c) CHECK=1 ;;
    *) sed -n '2,22p' "$0"; exit 0 ;;
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

posts=()
for folder in "${all_posts[@]}"; do
  [[ -n "$ONLY" ]] && ! in_list "$folder" "$ONLY" && continue
  in_list "$folder" "$SKIP" && continue
  spec="_journals/$JOURNAL/posts/$folder/spec.md"
  if [[ $FORCE -eq 0 && -f "$spec" ]] && grep -q "Sharpening pass" "$spec"; then
    echo "[done] $folder (already sharpened; -f to redo)"
    continue
  fi
  posts+=("$folder")
done

echo "${#posts[@]} post(s) to sharpen in $JOURNAL, $JOBS at a time"
[[ $DRY -eq 1 ]] && { printf '  %s\n' "${posts[@]}"; exit 0; }

ALLOWED=(
  Read Edit Write Grep Glob
  "Bash(python3:*)" "Bash(python3.11:*)"
  "Bash(git diff:*)" "Bash(git show:*)" "Bash(git status:*)"
  "Bash(grep:*)" "Bash(sed -n:*)" "Bash(wc:*)" "Bash(head:*)" "Bash(tail:*)" "Bash(ls:*)"
)

sharpen_one() {
  local folder="$1" file="_journals/$JOURNAL/posts/$1/index.md" log="$LOGDIR/$1.log"
  local start=$SECONDS
  echo "[start] $folder"
  # --allowedTools is variadic, so pass it as one comma-separated value and send the prompt on stdin.
  local tools
  tools="$(IFS=,; echo "${ALLOWED[*]}")"
  local args=(-p --permission-mode acceptEdits --no-session-persistence --allowedTools "$tools")
  [[ -n "$MODEL" ]] && args+=(--model "$MODEL")
  if printf '%s\n\n%s\n' "/sharpen-post $file" \
      "Run the skill autonomously on this one post: do not ask questions, do not edit other posts, do not commit. Finish with the skill's short report." \
      | claude "${args[@]}" >"$log" 2>&1; then
    echo "[ok]    $folder ($((SECONDS - start))s) — $LOGDIR/$folder.log"
  else
    echo "[fail]  $folder ($((SECONDS - start))s) — see $log"
  fi
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

echo "Rebuilding to confirm the journal still builds..."
python3 _wiring/build.py 2>&1 | grep -iE "$JOURNAL|error|Traceback" || true
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

if [[ $CHECK -eq 1 ]]; then
  echo "Checking headings and terms across chapters (read-only)..."
  check_args=(-p --no-session-persistence --allowedTools "Read,Grep,Glob")
  [[ -n "$MODEL" ]] && check_args+=(--model "$MODEL")
  printf '%s\n' "Read $OUTLINES: the heading outline of every chapter in _journals/$JOURNAL, in book order, after a sharpen-post pass that edited each chapter in isolation. Read _journals/$JOURNAL/README.md and any _research/style-guide.md or glossary post for the book's fixed terms. Report, without editing anything:
1. the same concept named differently in different chapters' headings (give both wordings, the chapters, and which wording to keep, preferring the glossary's);
2. headings in the same position across parallel pages (part intros, cases, hand-offs) that no longer share a shape;
3. headings that became vague or generic;
4. headings that look renamed but are still cited under the old name elsewhere (grep the posts to confirm).
Group findings by chapter folder, one line each, most important first. Say 'No issues' for a clean category." \
    | claude "${check_args[@]}" > "$LOGDIR/consistency.md" 2>&1 \
    && echo "Consistency report: $LOGDIR/consistency.md" \
    || echo "Consistency check failed; see $LOGDIR/consistency.md"
fi

echo "Done. Review with: git diff --stat -- _journals/$JOURNAL"
