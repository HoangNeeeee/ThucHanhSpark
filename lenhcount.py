from pyspark import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]") \
                    .appName('MyApp') \
                    .getOrCreate()

# Create a new SparkContext
sc=spark.sparkContext



# Create an RDD
rdd = sc.parallelize([1,2,3,4,5])

# Use the count() method to count the number of elements in the RDD
result = rdd.count()

# Print the result
print(result)