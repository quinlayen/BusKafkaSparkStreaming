# BusKafkaSparkStreaming

The Primary focus for this project was to build a real-time applicaiton that collects GPS data streamed by IoT Devices located on buses in the Toronto public bus system.  I chose route 7 because, well why not.

I chose to use Apache NiFi, CDC(Debezium), Kafka (MSK), Spark Structural Streaming, Docker, MySQL and visualization layer represented by Superset. The data source used in the project is TTC bus data from open API called Rest Bus. 

Some of the layers were not necessary to complete the final outcome and I could have condensed the pipeline into a more compact and streamlined format but I chose to use these technologies for learning purposes.


![](https://github.com/quinlayen/BusKafkaSparkStreaming/blob/master/architecture_diagram.png)
