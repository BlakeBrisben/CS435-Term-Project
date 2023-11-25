import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructField, StructType, LongType, BooleanType, DoubleType

if __name__ == "__main__":

    spark = SparkSession.builder.appName('CleanData').getOrCreate()

    input_schema = StructType([
        StructField('_c0', IntegerType(), True),
        StructField('app_id', LongType(), True),
        StructField('app_name', StringType(), True),
        StructField('review_id', LongType(), True),
        StructField('language', StringType(), True),
        StructField('review', StringType(), True),
        StructField('timestamp_created', LongType(), True),
        StructField('timestamp_updated', LongType(), True),
        StructField('recommended', BooleanType(), True),
        StructField('votes_helpful', IntegerType(), True),
        StructField('votes_funny', IntegerType(), True),
        StructField('weighted_vote_score', DoubleType(), True),
        StructField('comment_count', IntegerType(), True),
        StructField('steam_purchase', BooleanType(), True),
        StructField('received_for_free', BooleanType(), True),
        StructField('written_during_early_access', BooleanType(), True),
        StructField('author.steamid', LongType(), True),
        StructField('author.num_games_owned', IntegerType(), True),
        StructField('author.num_reviews', IntegerType(), True),
        StructField('author.playtime_forever', DoubleType(), True),
        StructField('author.playtime_last_two_weeks', DoubleType(), True),
        StructField('author.playtime_at_review', DoubleType(), True),
        StructField('author.last_played', DoubleType(), True)        
    ])

    output_schema = StructType([
        StructField('review', StringType(), True),
        StructField('recommended', BooleanType(), True)
    ])

    input_file_dir = sys.argv[1]
    output_file = sys.argv[2]
    print(f'Input File: {input_file_dir}\tOutput File: {output_file}')

    input_files = []
    for i in range(1,35):
        input_files.append('{}/steam_reviews-{}.csv'.format(input_file_dir, i))

    output_data = spark.createDataFrame([], output_schema)

    for f in input_files:
        input_data = spark.read.csv(f, header=False, schema=input_schema)
        print('read')
        #input_data.show()

        input_data = input_data.where(input_data.language == 'english')
        input_data = input_data.where(input_data.review != 'review')
        

        columns = input_data.columns
        columns_to_drop = []
        for i in range(len(columns)):
            if (columns[i] != 'review' and columns[i] != 'recommended') or 'author' in columns[i]:
                columns_to_drop.append(columns[i])

        curr_output_data = input_data.drop(*columns_to_drop)
        curr_output_data = curr_output_data.na.drop()

        output_data = output_data.union(curr_output_data).distinct()


    output_data.write.csv(output_file, header=True)

    