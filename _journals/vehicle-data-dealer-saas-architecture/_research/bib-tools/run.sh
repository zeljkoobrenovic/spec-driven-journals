#!/bin/sh
# Rebuild the bibliography of *Architecting a Vehicle Data and Dealer SaaS Platform* (posts/bibliography/index.md) from every page's "## Sources and Evidence".
# Usage, from anywhere:  sh _journals/vehicle-data-dealer-saas-architecture/_research/bib-tools/run.sh
# R-numbers stay stable through ids.json; see the header of gen.py.
set -e
cd "$(dirname "$0")"
python3 gen.py
python3 classify.py > classify-review.txt   # full topic/type listing, for review
python3 fix.py
python3 render.py
rm -f srcs2.json srcs3.json srcs4.json   # intermediates; ids.json is the only state to keep
