#!/bin/bash
input_dir="$1"
output_dit="$2"
find "$input_dir" -maxdepth 2 -type f -exec cp {} "$output_dir" \;
