# Twitter_Streaming_Kafka_Spark
My Insight Data Engineering project. I implemented a parallel big data processing pipelines , that streams real-time users data and load it to a PostgreSQL DATABASE using open source tools - ​Apache Kafka ​for data ingestions, and aggregates in specific window time  most popular hashtags world wide using open source tools - Apache Spark ​&amp; ​Spark Streaming ​for batch &amp; real-time processing.

## Architecture

![Diagram](https://user-images.githubusercontent.com/44294643/147892080-dde757ab-79a1-434a-a4b6-ce00872c659e.PNG)



## Install requirments

* Python version 3.7 (Otherwise you will not be able to use KafkaUtils sub-module)
* pyspark version 2.4.5
* kafka-python Client
* kafka_2.12-3.0.0.tgz
* WSL using Ubuntu distribution
 
## Set environment variables

```Bash
   sudo nano ~/.bashrc
```


```Bash
  export SPARK_HOME=/usr/local/spark
  export PATH=$PATH:$SPARK_HOME/bin
  
  export PYSPARK_PYTHON=/usr/bin/python3.7
  export PYSPARK_DRIVER_PYTHON=/usr/bin/python3.7 
 ```

## Run the following command

```Bash
  tar -xzf kafka_2.12-3.0.0.tgz
```


## Start ZooKeeper

```Bash
  cd kafka_2.12-3.0.0
  bin/zookeeper-server-start.sh config/zookeeper.properties
```


## Start the Kafka broker service

#### Start a new terminal 

```Bash
  cd kafka_2.12-3.0.0
  bin/kafka-server-start.sh config/server.properties
```


## Create relevant topics

#### start new terminal

* create tweets_topic

```Bash
  bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic tweets_topic --partitions 1 --replication-factor 1
```


* create users_topic

```Bash
  bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic users_topic --partitions 1 --replication-factor 1
```


## Run python scripts in parallel

#### Start new terminal

```Bash
  python3 tweet_producer.py
```

You should see something like this 

![Producer](https://user-images.githubusercontent.com/44294643/147891902-777da29a-8b56-42b7-b1aa-758cc0ac07a2.PNG)

#### Start another new terminal 

```Bash
  python3 tweet_consumer.py
```

You should be able to see something similar to this 

![consumer](https://user-images.githubusercontent.com/44294643/147891939-170ffe2c-d2a8-4c35-9f42-56626752dd3e.PNG)


## Run Spark Job

#### Start new terminal

```Bash
  spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0    tweet_spark_streaming.py
```

#### Some results

![streaming_results](https://user-images.githubusercontent.com/44294643/147891991-116cb68b-ae6a-4275-a894-ad801bbddf61.PNG)

![streaming_results2](https://user-images.githubusercontent.com/44294643/147892006-7c2256b6-118c-4302-81ca-2451d14e3e0c.PNG)

![streaming_results3](https://user-images.githubusercontent.com/44294643/147892010-f4518717-1815-4717-9943-92fd5956ae70.PNG)

![streaming_results4](https://user-images.githubusercontent.com/44294643/147892018-aaae4365-7a5a-450d-b7ed-aaf5c635cb12.PNG)

![streaming_results5](https://user-images.githubusercontent.com/44294643/147892019-c375fa3a-68a1-44cc-a01e-b35a93e19875.PNG)












