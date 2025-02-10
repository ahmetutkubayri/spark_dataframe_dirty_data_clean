from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import *

spark = SparkSession.builder \
.appName("Data Cleaning") \
.master("local[2]") \
.getOrCreate()

! wget -O /opt/examples/datasets/dirty_store_transactions.csv \
https://github.com/erkansirin78/datasets/raw/master/dirty_store_transactions.csv

df = spark.read.option("header", True) \
.option("inferSchema","true") \
.csv("file:///opt/examples/datasets/dirty_store_transactions.csv")

df.limit(2).toPandas()

df2 = df.select(
    F.regexp_replace(F.col("STORE_ID"), "[^a-zA-Z0-9,.-]", "").alias("STORE_ID"),
    F.regexp_replace(F.col("STORE_LOCATION"), "[^a-zA-Z0-9,.-]", "").alias("STORE_LOCATION"),
    F.regexp_replace(F.col("PRODUCT_CATEGORY"), "[^a-zA-Z0-9,.-]", "").alias("PRODUCT_CATEGORY"),
    F.col("PRODUCT_ID").cast(IntegerType()).alias("PRODUCT_ID"),
    F.regexp_replace(F.col("MRP"), "[^0-9.]", "").cast(FloatType()).alias("MRP"),
    F.regexp_replace(F.col("CP"), "[^0-9.]", "").cast(FloatType()).alias("CP"),
    F.regexp_replace(F.col("DISCOUNT"), "[^0-9.]", "").cast(FloatType()).alias("DISCOUNT"),
    F.regexp_replace(F.col("SP"), "[^0-9.]", "").cast(FloatType()).alias("SP"),
    F.to_date(F.col("Date"), "yyyy-MM-dd").alias("Date_Casted")
)

df2.limit(2).toPandas()

df2.show(1)

df2.printSchema()

df2.write \
.format("csv") \
.mode("overwrite") \
.option("header", "true") \
.save("file:///tmp/pyspark_output_data/cleaned_store_transactions.csv")

