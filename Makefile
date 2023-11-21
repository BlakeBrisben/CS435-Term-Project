
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

runTest:
	# add a scipt here for running a smaller sample dataset
	# ./runTest.sh

cleanData:
	clean_data.sh

resampleData:
	resample_data.sh

testData:
	make_test_datatset.sh

