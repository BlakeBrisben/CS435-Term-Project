# CS435-Term-Project
Term Project for CS435

Link to dataset: https://www.kaggle.com/datasets/najzeko/steam-reviews-2021

FilePartitioner.py: Place steam_reviews.csv in the parent directory of current and create a steam_reviews_part directory in the current directory to partition the data

### Run with spark-submit --master spark://MASTER.cs.colostate.edu:PORT CleanData.py /steam_reviews-part /cleaned_data
-Input csv: steam_reviews_part directory with files partitioned using FilePartitioner.py

-Output: /cleaned_data
