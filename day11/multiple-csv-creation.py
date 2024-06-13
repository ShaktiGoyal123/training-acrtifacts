
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import year

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Load the data
sparkdf = spark.read.csv('supplierdata.csv', header=True, inferSchema=True)
#sparkdf.show()

sparkdf.write.partitionBy("supplierYear").format("csv").save("supplierdata", mode="overwrite", header=True)
spark.stop()
sys.exit(0)


