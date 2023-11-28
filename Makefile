
 #code for stating the spark session the cluster
start:
	start-dfs.sh
	start-master.sh
	start-workers.sh
	jps

 #code for stopping the spark session on the cluster
stop:
	stop-master.sh
	stop-workers.sh
	stop-dfs.sh
	jps

cleanData:
	shell_scripts/clean_data.sh

resampleData:
	shell_scripts/resample_data.sh

testData:
	shell_scripts/make_test_datatset.sh

classifyData:
	shell_scripts/run_classifier.sh >> ./1_stats/classifier_stats.md

logReg:
	shell_scripts/run_logistic_regressionr.sh

rForest:
	shell_scripts/run_random_forest.sh

run:
	shell_scripts/run.sh
