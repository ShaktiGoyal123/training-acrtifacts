from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import sys

# Create a SparkSession
spark = SparkSession\
        .builder\
        .appName("FolderStream")\
        .master("local[*]")\
        .getOrCreate()

scm_schema=StructType([StructField("supplierId",IntegerType(),True),
                          StructField("supplierName",StringType(),True),
                          StructField("supplierEmail",StringType(),True),
                          StructField("supplierSharePrice",FloatType(),True)])

df_scm = spark.readStream\
        .format("csv")\
        .schema(scm_schema)\
        .option("header","true")\
        .option("maxFilesPerTrigger",1)\
        .load("/home/labuser/Documents/training-artifacts/training-acrtifacts/supporting-files")

        

print("Streaming ",df_scm.isStreaming)

print(df_scm.printSchema())

df_scm_01 = df_scm.groupBy("supplierId").agg(avg("supplierSharePrice").alias("TotalSharePrice"))

# result = df_scm_01.writeStream\
#           .format("console")\
#           .outputMode("complete")\
#           .start()

# complete line
result = df_scm.writeStream\
          .format("console")\
          .outputMode("append")\
          .start()

result.awaitTermination()
spark.stop()



# .load("C:\\Users\\SHAKTI_GOYAL\\Downloads\\csv_files_streaming")


