#!/bin/bash

python3 pix2pix.py \
  --mode train \
  --output_dir training_model \
  --max_epochs 200 \
  --input_dir dataset/train \
  --which_direction AtoB

python3 pix2pix.py \
  --mode test \
  --output_dir test_results \
  --input_dir dataset/val \
  --checkpoint training_model