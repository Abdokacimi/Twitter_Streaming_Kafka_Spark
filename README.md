# Twitter_Streaming_Kafka_Spark
My Insight Data Engineering project. I implemented a parallel big data processing pipelines , that streams real-time users data and load it to a PostgreSQL DATABASE using open source tools - ​Apache Kafka ​for data ingestions, and aggregates in specific window time  most popular hashtags world wide using open source tools - Apache Spark ​&amp; ​Spark Streaming ​for batch &amp; real-time processing.

## Install requirments

* Python version 3.7 (Otherwise will not be able to use KafkaUtils sub-module)
* pyspark version 2.4.5
* kafka-python Client
* kafka_2.12-3.0.0
* WSL using Ubuntu distribution
 
## Set environment variables

```Bash
  export SPARK_HOME=/usr/local/spark
  export PATH=$PATH:$SPARK_HOME/bin
  
  export PYSPARK_PYTHON=/usr/bin/python3.7
  export PYSPARK_DRIVER_PYTHON=/usr/bin/python3.7 
 ```
