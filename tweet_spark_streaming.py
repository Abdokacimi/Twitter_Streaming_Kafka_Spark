#! usr/bin/env python3
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from json import loads

sc = SparkContext(appName="Hashtag Streaming Application")

ssc = StreamingContext(sc, 10)

msg = KafkaUtils.createDirectStream(ssc, topics=['tweets_topic'], kafkaParams={
    "metadata.broker.list": "localhost:9092"
}, valueDecoder=lambda x: loads(x.decode('utf-8')))

tweetwords = msg.map(lambda x: x[1]).flatMap(lambda x: x.split(" "))

hashtags = tweetwords.filter(lambda x: x.startswith('#'))

hashtagsCount = hashtags.map(lambda x: (x, 1)).reduceByKey(
    lambda a, b: a+b).pprint()


ssc.start()

ssc.awaitTermination()
