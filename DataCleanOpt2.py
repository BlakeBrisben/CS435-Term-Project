import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

if __name__ == "__main__":

    spark = SparkSession.builder.appName('DataClean').getOrCreate()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f'Input File: {input_file}\tOutput File: {output_file}')

    input_data = spark.read.csv(input_file, header=True, inferSchema=True)

    input_data = input_data.where(input_data.language == 'english')

    output_data = input_data.select("app_name", "review", "recommended")

    output_data.na.drop()

    output_data.write.csv(output_file, header=True)

    spark.stop()