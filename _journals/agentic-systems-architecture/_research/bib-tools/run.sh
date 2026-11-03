#!/bin/sh
# Rebuild the bibliography of *Architecting Agentic Systems* (posts/bibliography/index.md) from every page's
# "## Sources and Evidence" section, and the human-review list review.txt.
# Usage, from anywhere:  sh _journals/agentic-systems-architecture/_research/bib-tools/run.sh [--links]
# R-numbers stay stable through ids.json; see the header of gen.py. Pages that are missing or still being
# written (no "## Sources and Evidence" section) are skipped and listed as SKIP.
set -e
cd "$(dirname "$0")"
python3 gen.py
python3 classify.py > classify-review.txt   # full topic/type listing, for review
python3 fix.py
python3 render.py
if [ "$1" = "--links" ]; then python3 check_links.py; fi   # optional: fetch every URL, flags go to review.txt
rm -f srcs2.json srcs3.json srcs4.json   # intermediates; ids.json is the only state to keep
