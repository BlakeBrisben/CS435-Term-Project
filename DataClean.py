import sys
from pyspark.sql import SparkSession

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

    input_data.printSchema()

    input_data = input_data.where(input_data.language == 'english')

    input_data.na.drop()

    input_data.write.csv(output_file, header=True)

    