import pyspark
from pyspark.sql import SQLContext
from pyspark import SparkContext,SparkConf

class Spark_handle():

    sc = pyspark.SparkContext('local[*]')
    sqlcontext = SQLContext(sc)
    twitter = sqlcontext.read.csv("TwitterData.csv",header = True).rdd
    google = sqlcontext.read.csv("GoogleTrendsCleaned.csv",header = True).rdd
