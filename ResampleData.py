import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":

    spark = SparkSession.builder.appName('ResampleData').getOrCreate()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f'Input File: {input_file}\tOutput File: {output_file}')

    input_data = spark.read.csv(input_file, header=True, inferSchema=True)

    input_data.show(4)
    input_data.printSchema()

    major_class_df = input_data.filter(input_data["recommended"] == "True")
    minor_class_df = input_data.filter(input_data["recommended"]  == "False")

    ratio = int(major_class_df.count()/minor_class_df.count())

    print("ratio: {}".format(ratio))

    # undersample the major class to be equal to the minor class

    major_class_sample = major_class_df.sample(fraction = 1/ratio)

    combined_df = major_class_sample.unionAll(minor_class_df)

    # new_major_class_df = combined_df.filter(combined_df["recommended"]  == "True")
    # new_minor_class_df = combined_df.filter(combined_df["recommended"]  == "False")


    # ratio = int(new_major_class_df.count()/new_minor_class_df.count())
    # print("new ratio: {}".format(ratio))
    # count = combined_df.count()
    # print("combined df count: {}".format(count))

    combined_df.write.csv(output_file, header=True)

    spark.stop()