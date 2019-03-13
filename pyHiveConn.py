# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:58:36 2018
使用pyspark直接连hive的数据库
@author: chenglong
"""

from pyspark import SparkConf, SparkContext 
from pyspark.sql import HiveContext 
from pyspark.sql import SparkSession
import numpy 
import scipy 
import pandas 
conf = (SparkConf() 
         .setMaster("yarn")
         .setAppName("Python hive connection") 
         .set("spark.executor.memory", "1g")) 
#spark = SparkSession 
#            .builder\ 
#            .enableHiveSupport()\ 
#            .getOrCreate()
#spark = SparkSession.builder.appName("Hive debug").config("hive.metastore.uris","thrift://10.3.2.64:9083").enableHiveSupport().getOrCreate()



spark = SparkSession.builder.appName("Hive debug").config("hive.metastore.uris","thrift://10.3.2.64:9083").enableHiveSupport().getOrCreate()
hc = HiveContext(spark)
mydata = hc.sql("show tables")
mydata.show()


#sc = SparkContext(conf = conf) 
sqlContext = HiveContext(hc) 
my_dataframe = sqlContext.sql("show tables") 

my_dataframe2= sqlContext.sql("show tables")
print('next row')
my_dataframe2.show() 



print("here is")
#my_dataframe3=sqlContext.sql("create  table tabeldemo(id int)")
print("这里创建护数据")


#my_dataframe3.show()  
print('下一行')


my_dataframe4= sqlContext.sql("show tables")

#print("luopeng's table")

#my_dataframe4.show()  
print('下一行')

my_dataframe41= sqlContext.sql("show tables")
print("luopeng's table")
my_dataframe41.show()  

print("insert into start")
my_dataframe5= sqlContext.sql("insert into tabeldemo values(11)")
print("insert into 5end")
my_dataframe5.show()

my_dataframe51= sqlContext.sql("insert into tabeldemo values(11)")
print("insert into 51end")
my_dataframe51.show()

my_dataframe52= sqlContext.sql("insert into tabeldemo values(11)")
print("insert into 52end")
my_dataframe52.show()
my_dataframe53= sqlContext.sql("insert into tabeldemo values(11)")
print("insert into 53end")
my_dataframe53.show()
my_dataframe54= sqlContext.sql("insert into tabeldemo values(11)")
print("insert into 54end")
my_dataframe54.show()
my_dataframe55= sqlContext.sql("insert into tabeldemo values(11)")
print("insert into 55end")
my_dataframe55.show()



my_dataframe6= sqlContext.sql("show tables")
my_dataframe6.show()

my_dataframe7= sqlContext.sql("desc tabeldemo")

print("select start")
my_dataframe8= sqlContext.sql("select * from tabeldemo")
print("select end")


#my_dataframe3.show() 
print('下一行')
my_dataframe4.show() 
print('下一行')
my_dataframe6.show() 
print('下一行')
#my_dataframe7.show() 
print('7不打了下一行')
my_dataframe8.show() 

print('下一xxxxx行')

#my_dataframe3.show() 
print('my_dataframe3下一行')
my_dataframe4.show() 
print('my_dataframe4下一行')
my_dataframe6.show() 
print('my_dataframe6下一行')
#my_dataframe7.show() 
print('7不打了 my_dataframe7下一行')
my_dataframe8.show() 



spark.stop()
#outputCommitCoordinator.handleAskPermissionToCommit(stage, partition, attemptNumber))