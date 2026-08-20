#!/usr/bin/env bash
# Run this from inside the unzipped artifact-repo folder, after you've created
# an empty repo on github.com (see the instructions in the chat).
#
# Usage:
#   chmod +x push_to_github.sh
#   ./push_to_github.sh https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git

set -euo pipefail

if [ -z "${1:-}" ]; then
  echo "Usage: ./push_to_github.sh <your-empty-repo-url>"
  echo "Example: ./push_to_github.sh https://github.com/jdoe/cfo-office-agent-coverage.git"
  exit 1
fi

REPO_URL="$1"

git init -q
git add -A
git commit -q -m "Initial release: CFO-office agent coverage matrix and governance scorecard"
git branch -M main
git remote add origin "$REPO_URL"
git push -u origin main

echo ""
echo "Pushed. Verify at: ${REPO_URL%.git}"
echo "Next: go to https://anonymous.4open.science/ and anonymize this repo."
