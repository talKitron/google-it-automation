#!/bin/bash

for file in *.HTML; do
  name=$(basename "$file" .HTML)
  echo mv "$file" "$name.html"
done
