from pyspark.sql import SparkSession

# Tạo SparkSession object
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Tạo RDD từ list các số nguyên
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])

# Áp dụng hàm square lên các phần tử của RDD
squared_rdd = rdd.map(lambda x: x**2)

# In ra kết quả
print(squared_rdd.collect())