# CS435-Term-Project
Term Project for CS435

Link to dataset: https://www.kaggle.com/datasets/najzeko/steam-reviews-2021

FilePartitioner.py: Place steam_reviews.csv in the parent directory of current and create a steam_reviews_part directory in the current directory to partition the data

### Run with spark-submit --master spark://MASTER.cs.colostate.edu:PORT CleanData.py -OPT /INPUT_FILE /OUTPUT_FILE

-OPT: Either 
    -p: For partitioned files, the input file will be a directory of the partitioned .csv files
    -w: For whole data files, the input file will be a .csv file
