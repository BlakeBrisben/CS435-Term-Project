#!/bin/bash

MASTER=$(cat "./MasterName.txt")

spark-submit --master $MASTER DataClean.py /TP/input_data/steam_reviews.csv.gz /TP/output/output_cleaned_data