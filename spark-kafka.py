df = spark.\
     readStream \
     .format("kafka") \
     .option("kafka.bootstrap.servers", "kafka:9092") \
     .option("subscribe", "dbserver1.demo.bus_status") \
     .load()
df.printSchema()