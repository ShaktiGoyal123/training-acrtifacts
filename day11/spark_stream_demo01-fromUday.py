from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

#spark.sql.streaming.forceDeleteTempCheckpointLocation: True

spark = SparkSession \
    .builder \
    .appName("demodellproducts-app") \
    .getOrCreate()

try:

    products_ds = spark \
        .readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", 9999) \
        .load()

    print("Started Streaming : ",products_ds.isStreaming)

    product_list = products_ds.select(
    explode(
        split(products_ds.value, " ")
    ).alias("product")
    )


    df_products = product_list.groupBy("product").count()

    # run the query that prints the products and its count to console

    query = df_products \
        .writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()

    query.awaitTermination()

except Exception as ex:
    print("Error occured while connecting to the data server",ex)
finally:
    spark.stop()