#!/bin/bash
input_dir="$1"
output_dit="$2"
for f in $(find $input_dir);
  do  cp $f $output_dir;
done
