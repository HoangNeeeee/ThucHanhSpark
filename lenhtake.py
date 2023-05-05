from pyspark.sql import SparkSession

# Tạo SparkSession object
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Tạo RDD từ list các số nguyên
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Lấy 5 phần tử đầu tiên của RDD
first_five = rdd.take(5)

# In ra kết quả
print(first_five)