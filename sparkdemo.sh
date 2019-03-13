#!/bin/bash

cd $JOB_WORKING_DIR
export HADOOP_CONF_DIR=$JOB_WORKING_DIR/hadoop_conf
export HADOOP_USER_NAME=hdfs
export JAVA_HOME=/opt/bdp/deploy/jdk

/opt/bdp/deploy/spark-client/bin/spark-submit --master yarn --deploy-mode cluster --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=/home/disk5/anaconda2/bin/python $JOB_WORKING_DIR/pyHiveConn.py 
