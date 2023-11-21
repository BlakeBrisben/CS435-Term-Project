import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":

    spark = SparkSession.builder.appName('MakeTestData').getOrCreate()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f'Input File: {input_file}\tOutput File: {output_file}')

    input_data = spark.read.csv(input_file, header=True, inferSchema=True)

    smaller_sample_df = input_data.sample(fraction = 0.1)

    

    smaller_sample_df.coalesce(1).write.csv(output_file, header=True, compression = "gzip")