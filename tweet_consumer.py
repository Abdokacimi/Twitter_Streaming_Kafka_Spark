#! usr/bin/env python3
from kafka import KafkaConsumer
from json import loads
import pandas as pd
import tweet_load as load
user_data = []

# We just need to define and create a KafkaConsumer subscribing to the topic tweets_topic
consumer = KafkaConsumer(
    "users_topic", value_deserializer=lambda x: loads(x.decode('utf-8')), auto_offset_reset='earliest',)

for i, msg in enumerate(consumer):
    if i == 19:
        break
    user_data.append(msg.value)
    print(msg.value)

consumer.close()

if (consumer._closed):
    print("consumer closed !")

df_users = pd.DataFrame(user_data)

df_users.to_csv('twitter_data.csv', index=False)

load.load_to_db('twitter_data.csv')
