#!/usr/bin/env bash
set -uo pipefail
mkdir -p /workspace/.hf_home/hub
for d in /workspace/.hf_home/models--*; do
  [[ -d "$d" ]] || continue
  base="$(basename "$d")"
  dest="/workspace/.hf_home/hub/$base"
  if [[ ! -e "$dest" ]]; then
    ln -s "$d" "$dest"
    echo "linked $base"
  fi
done
echo HUB
ls /workspace/.hf_home/hub | grep models-- || true
