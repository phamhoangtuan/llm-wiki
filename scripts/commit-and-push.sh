#!/usr/bin/env bash
set -Eeuo pipefail

usage() {
	printf 'Usage: %s "commit message"\n' "$(basename "$0")" >&2
	exit 2
}

message=${*:-}
[[ -n "$message" ]] || usage

root=$(git rev-parse --show-toplevel)
cd "$root"

branch=$(git branch --show-current)
[[ -n "$branch" ]] || {
	printf 'Refusing to push from detached HEAD.\n' >&2
	exit 1
}

git add -A

if git diff --cached --quiet; then
	printf 'Nothing to commit.\n'
	exit 0
fi

git diff --cached --check
git commit -m "$message"
git push -u origin "$branch"
