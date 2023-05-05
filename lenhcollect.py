from pyspark import SparkContext
from pyspark.sql import SparkSession
sc = SparkContext() 
# Tạo một RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# Sử dụng lệnh collect để lấy tất cả các phần tử từ RDD và trả về một mảng
result = rdd.collect()
# In kết quả
print(result)