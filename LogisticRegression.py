import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import rand

from pyspark.ml import Pipeline
from pyspark.ml.feature import StopWordsRemover, RegexTokenizer, HashingTF, IDF
from pyspark.ml.classification import RandomForestClassifier, LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

from sklearn.metrics import classification_report

import pandas

if __name__ == "__main__":

    spark = spark = SparkSession.builder.appName('Class').getOrCreate()

    print("start of logistic regression classification")

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

    df = df.orderBy(rand())

    df.show(10)

    def logisticRegressionCrossValidation(df, folds = 5):
       
       (train, test) = df.randomSplit([0.80, 0.20])

       lr = LogisticRegression(featuresCol='features', labelCol='label', family="auto")
       pipeline = Pipeline(stages = [lr])
       grid = ParamGridBuilder() \
               .addGrid(lr.regParam, [0.1, 0.2, 0.3]) \
               .addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0]) \
               .addGrid(lr.maxIter, [10, 20, 50, 70]) \
               .build()
       evaluator = BinaryClassificationEvaluator(labelCol = "label")
       cross_validator = CrossValidator(estimator = pipeline, 
                                        evaluator = evaluator, 
                                        estimatorParamMaps = grid,
                                         numFolds = folds)
    #    cv_model = cross_validator.fit(df)
    #    predictions = cv_model.transform(df)
    #    predictions.select("label", "probability", "prediction").show(10)
    #    accuracy = evaluator.evaluate(predictions)

       cv_model = cross_validator.fit(train)
       best_model = cv_model.bestModel.stages[0]
       predictions = best_model.transform(test)
       predictions.select("label", "probability", "prediction").show(10)
       accuracy = evaluator.evaluate(predictions)

       print("Cross validation accuracy: " + str(accuracy))
       print()

       preds_df = predictions.select('app_name','review',"label", "prediction").toPandas()
       predictions = predictions.select('app_name',"label", "prediction")
       print (classification_report(preds_df['label'], preds_df['prediction']))

    #    best_model = cv_model.bestModel.stages[0]

       print("Best reg: " + str(best_model.getRegParam()))
       print("Best Max Iterations: " + str(best_model.getMaxIter()))
       print("Best elasticNet: " + str(best_model.getElasticNetParam()))
       print("Best family: " + str(best_model.getFamily()))

       return predictions
    
    predictions = logisticRegressionCrossValidation(df, folds = 5)

    predictions.repartition(1).write.csv(output_file, header=True, compression = "gzip")

    print("end of logistic regression classification")

    spark.stop()