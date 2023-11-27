import sys

import seaborn as sns
import matplotlib.pyplot as plt

from pyspark.sql import SparkSession

from pyspark.sql.types import FloatType
from pyspark.sql.functions import col, rand
from pyspark.ml import Pipeline
from pyspark.ml.feature import StopWordsRemover, RegexTokenizer, HashingTF, IDF

import pandas as pd

from pyspark.ml.classification import RandomForestClassifier, LogisticRegression
from pyspark.mllib.evaluation import MulticlassMetrics

from sklearn.metrics import classification_report

if __name__ == "__main__":

    spark = spark = SparkSession.builder.appName('Class').getOrCreate()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f'Input File: {input_file}\tOutput File: {output_file}')

    spark

    input_data = spark.read.csv(input_file, header=True, inferSchema=True)

    input_data.show(10)

    df = input_data

    tokenizer = RegexTokenizer(inputCol="review", outputCol="words", pattern="\\W")

    stopwords_remover = StopWordsRemover(inputCol="words", outputCol="filtered")

    hashing_tf = HashingTF(inputCol="filtered",
        outputCol="raw_features", numFeatures=10000)

    idf = IDF(inputCol="raw_features", outputCol="features")

    preprocessing_pipeline = Pipeline(
        stages=[
            tokenizer,
            stopwords_remover,
            hashing_tf,
            idf])

    df = preprocessing_pipeline.fit(df).transform(df)

    df.show(10)

    df.select("review").show(10, truncate = False )

    df.select("filtered").show(10, truncate = False )

    df = df.orderBy(rand())

    df.show(10)

    (train, test) = df.randomSplit([0.75, 0.25], seed = 202)

    def RandomForest(train, test):
      rf = RandomForestClassifier(labelCol='label', featuresCol='features', numTrees=20, impurity="gini")
      rf_model = rf.fit(train)
      predictions = rf_model.transform(test)
      return predictions

    # df_pred = RandomForest(train, test)

    def logisticRegression(train, test):
        lr = LogisticRegression(featuresCol='features',
                                labelCol='label',
                                family="multinomial",
                                regParam=0.2,
                                elasticNetParam=0,
                                maxIter=50)
        lrModel = lr.fit(train)
        predictions = lrModel.transform(test)

        return predictions

    predictions = logisticRegression(train, test)

    # predictions = RandomForest(train, test)

    predictions.select("label", "probability", "prediction").show(10)

    preds_df = predictions.select('app_name','review',"label", "prediction").toPandas()

    predictions = predictions.select('app_name',"label", "prediction")

    print (classification_report(preds_df['label'], preds_df['prediction']))

    predictions.repartition(1).write.csv(output_file, header=True, compression = "gzip")

    spark.stop()