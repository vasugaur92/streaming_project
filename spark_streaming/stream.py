from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PrintKafkaMessages").getOrCreate()

df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka-broker:29092")
    .option("subscribe", "my-topic")
    .option("startingOffsets", "latest")
    .load()
)

messages = df.selectExpr("CAST(value AS STRING) AS message")

messages.writeStream.format("console").start().awaitTermination()
