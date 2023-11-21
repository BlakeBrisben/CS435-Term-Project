#!/bin/bash

MASTER=$(cat "./MasterName.txt")

spark-submit --master $MASTER ResampleData.py /TP/output/resampled_data/* /TP/output/test_sample