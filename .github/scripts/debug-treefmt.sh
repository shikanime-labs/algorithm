#!/usr/bin/env bash
set -uo pipefail
# Run treefmt in WRITE mode (not --check) so all formatters apply their
# changes to disk. zizmor will rewrite the 2 workflow YAMLs and exit 1, but the
# other formatters still write their changes first. `|| true` keeps us alive.
treefmt --tree-root=. --walk=git 2>&1 | tail -8 || true
echo "=== GIT STATUS (all files formatters changed) ==="
git --no-pager status --short
