import sys
import sparknlp

import seaborn as sns
import matplotlib.pyplot as plt

from pyspark.sql.types import FloatType
from pyspark.sql.functions import col, when, rand
from pyspark.ml import Pipeline

from pyspark.ml.feature import StopWordsRemover, HashingTF, IDF

from sparknlp.annotator import *
from sparknlp.base import *

import pandas as pd

from pyspark.ml.classification import RandomForestClassifier, LogisticRegression
from pyspark.mllib.evaluation import MulticlassMetrics

from sklearn.metrics import classification_report

if __name__ == "__main__":

    spark = sparknlp.start()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    print(f'Input File: {input_file}\tOutput File: {output_file}')

    spark

    input_data = spark.read.csv(input_file, header=True, inferSchema=True)

    input_data.show(10)

    df = input_data

    document_assembler = DocumentAssembler() \
        .setInputCol("review") \
        .setOutputCol("document")

    tokenizer = Tokenizer() \
        .setInputCols(["document"]) \
        .setOutputCol("token")

    normalizer = Normalizer() \
        .setInputCols(["token"]) \
        .setOutputCol("normalized") \
        .setLowercase(True)

    stopwords_cleaner = StopWordsCleaner()\
        .setInputCols("normalized")\
        .setOutputCol("normalized_Tokens")\
        .setCaseSensitive(False)

    lemma = LemmatizerModel.pretrained('lemma_antbnc') \
        .setInputCols(["normalized_Tokens"]) \
        .setOutputCol("lemma")

    finisher = Finisher() \
        .setInputCols(["lemma"]) \
        .setOutputCols(["filtered"]) \
        .setValueSplitSymbol(" ")

    hashing_tf = HashingTF(inputCol="filtered",
        outputCol="raw_features", numFeatures=10000)

    idf = IDF(inputCol="raw_features", outputCol="features")

    preprocessing_pipeline = Pipeline(
        stages=[
            document_assembler,
            tokenizer,
            normalizer,
            stopwords_cleaner,
            lemma,
            finisher,
            hashing_tf,
            idf])

    df = preprocessing_pipeline.fit(df).transform(df)

    df.show(10)

    df.select("review").show(10, truncate = False )

    df.select("filtered").show(10, truncate = False )

    df = df.orderBy(rand())

    df.show(10)

    (train, test) = df.randomSplit([0.75, 0.25], seed = 202)

    # def RandomForest(train, test):
    #   rf = RandomForestClassifier(labelCol='recommended', featuresCol='features', numTrees=20, impurity="gini")
    #   rf_model = rf.fit(train)
    #   predictions = rf_model.transform(test)
    #   return predictions

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

    predictions.select("label", "probability", "prediction").show(10)

    labels = ["recommended", "not recommended"]

    # important: need to cast to float type, and order by prediction, else it won't work
    preds_and_labels = predictions.select(['prediction','label']) \
                                .withColumn('label', col('label') \
                                .cast(FloatType())) \
                                .orderBy('prediction')

    _ = plt.figure(figsize=(7, 7))

    metrics = MulticlassMetrics(preds_and_labels.rdd.map(tuple))

    # plot confusion matrix
    sns.heatmap(metrics.confusionMatrix().toArray(),
                cmap='viridis',
                annot=True,fmt='0',
                cbar=False,
                xticklabels=labels,
                yticklabels=labels)
    plt.show()

    preds_df = predictions.select('app_name','review',"label", "prediction").toPandas()

    print (classification_report(preds_df['label'], preds_df['prediction']))

    spark.stop()

    predictions.write.csv(output_file, header=True)

    spark.stop()