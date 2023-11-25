
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

# removes all files in the hadoop output folder for the term project
deleteOutput:
	hadoop fs -rm -r /TP/output/* | echo "**Output folder is already empty!**"

