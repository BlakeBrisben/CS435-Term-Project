import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, StringType, StructField, StructType, LongType, BooleanType, DoubleType
import numpy as np

def part_file_read(input_file_dir):
    input_files = []
    for i in range(1,35):
        input_files.append('{}/steam_reviews-{}.csv'.format(input_file_dir, i))

    output_data = spark.createDataFrame([], get_out_schema())

    for f in input_files:
        input_data = spark.read.csv(f, header=False, schema=get_in_schema())
        #print('read')
        #input_data.show()

        curr_output_data = clean(input_data)

        output_data = output_data.union(curr_output_data).distinct()

    return output_data

def whole_file_read(input_file):
    output_data = spark.createDataFrame([], get_out_schema())

    input_data = spark.read.csv(input_file, header=False, schema=get_in_schema())

    output_data = clean(input_data)

    return output_data

def drop_cols(input_data, columns_to_keep):
    columns = input_data.columns
    #new_cols=(column.replace('.', '_') for column in columns)
    columns_to_drop = []
    columns_to_drop = np.setdiff1d(columns, columns_to_keep)

    output_data = input_data.drop(*columns_to_drop)

    return output_data

def clean(input_data):
    columns = input_data.columns
    output_data = input_data.where(input_data.language == 'english')
    output_data = output_data.where(output_data.review != 'review')

    output_data = drop_cols(output_data, ['app_name', 'review', 'recommended'])

    output_data = output_data.na.drop()
    output_data = output_data.filter(output_data.review.rlike("\\w+"))

    return output_data
    

def get_in_schema():
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
        StructField('author_steamid', LongType(), True),
        StructField('author_num_games_owned', IntegerType(), True),
        StructField('author_num_reviews', IntegerType(), True),
        StructField('author_playtime_forever', DoubleType(), True),
        StructField('author_playtime_last_two_weeks', DoubleType(), True),
        StructField('author_playtime_at_review', DoubleType(), True),
        StructField('author_last_played', DoubleType(), True)        
    ])

    return input_schema

def get_out_schema():
    output_schema = StructType([
        StructField('app_name', StringType(), True),
        StructField('review', StringType(), True),
        StructField('recommended', BooleanType(), True)
    ])

    return output_schema




if __name__ == "__main__":

    spark = SparkSession.builder.appName('CleanData').getOrCreate()    

    opts = [opt for opt in sys.argv[1:] if opt.startswith('-')]
    args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
    input_file = args[0]
    output_file = args[1]
    print(f'Input File: {input_file}\tOutput File: {output_file}')

    if len(opts) < 1:
        raise ValueError('No option given: Please give -p: for partitioned data or -w: for a whole file')

    if opts[0] == '-p':
        output_data = part_file_read(input_file)
    elif opts[0] == '-w':
        output_data = whole_file_read(input_file)
    else:
        raise ValueError('Invalid option given: Please give -p: for partitioned data or -w: for a whole file')

    output_data.write.csv(output_file, header=True)

    