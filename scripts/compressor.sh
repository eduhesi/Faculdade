#!/bin/bash

start_path="${1:-.}"

dirs=()
while IFS= read -r -d '' dir; do
  dirs+=("$dir")
done < <(find "$start_path" -maxdepth 1 -type d -print0)

for dir in "${dirs[@]}"; do
  [[ "$dir" == "$start_path" ]] && continue
  base_dir="$(basename "$dir")"
  tar -czf "${base_dir}.tar.gz" -C "$start_path" "$base_dir"
done