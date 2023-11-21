#!/bin/bash

MASTER=$(cat "./MasterName.txt")

spark-submit --master $MASTER ResampleData.py /TP/output/output_cleaned_data/* /TP/output/resampled_data