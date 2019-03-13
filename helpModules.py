# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:59:10 2018

@author: chenglong
"""
from pyspark.sql import SparkSession
help("modules")
spark = SparkSession\
    .builder\
    .appName("PythonPi")\
    .getOrCreate()
spark.stop()