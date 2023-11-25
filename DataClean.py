import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

if __name__ == "__main__":

    spark = SparkSession.builder.appName('DataClean').getOrCreate()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f'Input File: {input_file}\tOutput File: {output_file}')

    input_data = spark.read.csv(input_file, header=True, inferSchema=True)

    input_data.printSchema()

    for col in input_data.dtypes:
        if 'author' in col[0]:
            input_data = input_data.drop(col[0])
            print(col[0])

    input_data = input_data.where(input_data.language == 'english')

    input_data.na.drop()

    #drop all colum except the name of the game, the review, and recommended status
    cols_to_drop = ("_c0", "app_id","language", "timestamp_created", "review_id", 
                    "timestamp_updated", "votes_helpful", "votes_funny", "weighted_vote_score", 
                    "comment_count", "received_for_free", "written_during_early_access", "steam_purchase")
    
    cleaned_data = input_data.drop(*cols_to_drop)
    cleaned_data.show(10)
    cleaned_data.printSchema()

    cleaned_data.write.csv(output_file, header=True)

    spark.stop()