#!/usr/bin/env bash

set -e

# assert the trang command exists
if ! [ -x "$(command -v trang)" ]; then
  echo 'trang command not found; please install'
  exit 1
fi

# iterate through changed rnc files
for rncfile in $(git diff --cached --name-only | grep -E '\.rnc$')
do
  rngfile="${rncfile//+(*\/|.*)}.rng"
  trang "$rncfile" "$rngfile" && trang "$rngfile" "$rncfile"
  rm -f "$rngfile"
  git add "$rncfile"
done

