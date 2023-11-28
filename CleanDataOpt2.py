import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

if __name__ == "__main__":

    spark = SparkSession.builder.appName('DataClean').getOrCreate()

    print("start of the data cleaning process")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print(f'Input File: {input_file}\tOutput File: {output_file}')

    input_data = spark.read.csv(input_file, header=True, inferSchema=True)

    input_data.printSchema()

    print("Total number of observations before cleaning: " + str(input_data.count()))

    input_data = input_data.where(input_data.language == 'english')

    output_data = input_data.select("app_name", "review", "recommended")

    output_data = output_data.filter(col("review").rlike("\\w+"))

    output_data = output_data.na.drop()

    print("Total number of observations after cleaning: " + str(output_data.count()))

    output_data.show(10)

    output_data.write.csv(output_file, header=True)

    print("end of the data cleaning process")

    spark.stop()