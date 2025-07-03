#!/usr/bin/env bash
set -e
main_branch="main"

# 1. pull latest
git checkout "$main_branch"
git pull origin "$main_branch"

# 2. list merged branches, exclude main & protected
merged=$(git branch --merged | grep -vE "$main_branch|dev|release" | tr -d '* ')
echo "Deleting merged branches:"
echo "$merged"
# 3. delete local & remote
for b in $merged; do
  git branch -d "$b"
  git push origin --delete "$b" || true
done
echo "✅  All merged branches cleaned up."
