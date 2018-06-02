#!/bin/bash

# Record amount of images users wants for training/test data
PERCENT_TRAINING="0.8"
PERCENT_TEST="0.2"
if [[ "${NUM_ARGS}" -eq 1 ]]; then
  # Check 
  if [[ "$2" =~ ^[0-9]+(\.[0-9]+)?$ ]] && (( $(echo "$2 >= 0" | bc -l) )) \
    && (( $(echo "$2 <= 1" | bc -l) ));
  then
    PERCENT_TRAINING=$(echo "$2" | bc -l )
    PERCENT_TEST=$(echo "1 - $2" | bc -l )
  fi
fi

# Split into train/val set
python3 tools/split.py \
  --train_frac "${PERCENT_TRAINING}" \
  --test_frac "${PERCENT_TEST}" \
  --dir dataset