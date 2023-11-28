import sys
from pyspark.sql import SparkSession

from pyspark.sql.functions import when

if __name__ == "__main__":

    spark = SparkSession.builder.appName('ResampleData').getOrCreate()

    print('start of the resampling process')

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f'Input File: {input_file}\tOutput File: {output_file}')

    input_data = spark.read.csv(input_file, header=True, inferSchema=True)

    print("Total number of observations before resampling: " + str(input_data.count()))

    input_data.show(4)
    input_data.printSchema()

    major_class_df = input_data.filter(input_data["recommended"] == "True")
    minor_class_df = input_data.filter(input_data["recommended"]  == "False")

    major_count = major_class_df.count()
    minor_count = minor_class_df.count()

    print("Total number of recommended games before resampling: " + str(major_count))
    print("Total number of not recommended games before resampling: " + str(minor_count))

    ratio = int(major_count/minor_count)

    print("ratio: {}".format(ratio))

    # undersample the major class to be equal to the minor class

    major_class_sample = major_class_df.sample(fraction = 1/ratio)

    combined_df = major_class_sample.unionAll(minor_class_df)

    combined_df = combined_df.withColumn("recommended", when(combined_df.recommended==True, 1).otherwise(0))

    combined_df = combined_df.withColumnRenamed("recommended", "label")

    print("Total number of observations after resampling: " + str(combined_df.count()))

    final_major_count = combined_df.filter(combined_df["label"] == 1).count()
    final_minor_count = combined_df.filter(combined_df["label"] == 0).count()

    print("Total number of recommended games after resampling: " + str(final_major_count))
    print("Total number of not recommended games after resampling: " + str(final_minor_count))
    print("resampled ratio: " + str(int(final_major_count/final_minor_count)))
    
    combined_df.printSchema()
    combined_df.show(4)

    combined_df.write.csv(output_file, header=True)

    print('end of the resampling process')

    spark.stop()