from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

# Create a SparkSession
spark = SparkSession.\
        builder.\
        appName("demo-dellproducts-app").\
        getOrCreate()

try:
# hold the stream stream data frame from a server
    products_ds = spark.readStream\
        .format("socket")\
        .option("host", "localhost")\
        .option("port", 9999)\
        .load()

    print("Started Streming data from the server",products_ds.isStreaming)

    products_list= products_ds.select(explode
                (split(products_ds.value, " ")).
                alias("product"))

    df_products = products_list.groupBy("product").count()

    query = df_products\
                .writeStream\
                .outputMode("complete")\
                .format("console")\
                .start()

    query.awaitTermination()
    spark.stop()
except Exception as e:
    print("Error occured", e)

