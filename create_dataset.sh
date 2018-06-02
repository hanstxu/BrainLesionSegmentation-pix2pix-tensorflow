#!/bin/bash

# Check for at least one command-line arguments
NUM_ARGS="$#"
if [[ "${NUM_ARGS}" -lt 2 ]]; then
  echo "Error: Missing command-line arguments"
  exit
fi

# Check input files are a directory
INPUT_DIR="$1"
if [[ ! -d "${INPUT_DIR}" ]]; then
  echo "Error: File is not a directory or not found"
  exit
fi

B_DIR="$2"
if [[ ! -d "${B_DIR}" ]]; then
  echo "Error: File is not a directory or not found"
  exit
fi

python3 tools/process.py \
  --input_dir "${INPUT_DIR}" \
  --b_dir "${B_DIR}" \
  --operation combine \
  --output_dir dataset