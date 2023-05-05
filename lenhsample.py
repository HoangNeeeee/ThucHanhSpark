from pyspark.sql import SparkSession

# Tạo SparkSession object
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Tạo RDD từ list các số nguyên
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Lấy mẫu ngẫu nhiên 3 phần tử từ RDD
sample = rdd.sample(False, 0.2, seed=42)

# In ra kết quả
print(sample.collect())