#!/bin/bash

dirs=()
while IFS= read -r -d '' dir; do
  dirs+=("$dir")
done < <(find . -maxdepth 1 -type d -print0)

for dir in "${dirs[@]}"; do
  [[ "$dir" == "." ]] && continue
  tar -czf "${dir##./}.tar.gz" "$dir"
done