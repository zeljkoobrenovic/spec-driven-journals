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
#
# Logs go to _temp/sharpen-post/<journal>/<folder>.log. Nothing is committed:
# review the result with git diff.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
cd "$ROOT"

JOBS=1 MODEL="" ONLY="" SKIP="bibliography,glossary" FORCE=0 DRY=0
while getopts "j:m:o:s:fnh" opt; do
  case "$opt" in
    j) JOBS="$OPTARG" ;;
    m) MODEL="$OPTARG" ;;
    o) ONLY="$OPTARG" ;;
    s) SKIP="$OPTARG" ;;
    f) FORCE=1 ;;
    n) DRY=1 ;;
    *) sed -n '2,19p' "$0"; exit 0 ;;
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
posts=()
while IFS= read -r folder; do
  [[ -n "$ONLY" ]] && ! in_list "$folder" "$ONLY" && continue
  in_list "$folder" "$SKIP" && continue
  spec="_journals/$JOURNAL/posts/$folder/spec.md"
  if [[ $FORCE -eq 0 && -f "$spec" ]] && grep -q "Sharpening pass" "$spec"; then
    echo "[done] $folder (already sharpened; -f to redo)"
    continue
  fi
  posts+=("$folder")
done < <(sed -nE 's#^[[:space:]]*-[[:space:]]+([^/[:space:]]+)/index\.md[[:space:]]*$#\1#p' "$CONFIG")

echo "${#posts[@]} post(s) to sharpen in $JOURNAL, $JOBS at a time"
[[ $DRY -eq 1 ]] && { printf '  %s\n' "${posts[@]}"; exit 0; }
[[ ${#posts[@]} -eq 0 ]] && exit 0

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

if [[ "$JOBS" -le 1 ]]; then
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
echo "Done. Review with: git diff --stat -- _journals/$JOURNAL"
