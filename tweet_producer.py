#! usr/bin/env python3
import tweepy
from tweepy.streaming import Stream
import time
from kafka import KafkaProducer
import json

# Set up your credentials from https://developer.twitter.com
CONSUMER_KEY = " "
CONSUMER_SECRET = " "
ACCESS_TOKEN = " "
ACCESS_SECRET = " "


# we can now start producing messages to tweets_topic
tweets_producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# producing users data to users_topic
users_producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# we will be using this list to control and close the streaming session
tweet_list = []


class myStream(tweepy.Stream):

    def on_status(self, status):
        try:
            users_producer.send('users_topic', {'user_id': str(
                status.user.id), 'username': status.user.name, 'tweet': status.text[:20], 'created_at': str(status.created_at)})
            tweets_producer.send('tweets_topic', status.text)
            tweet_list.append(status.text)
            print(" length of tweet_list is : ", len(tweet_list))
            print(str(status.user.id)+'    '+status.user.name+'    ' +
                  status.text[:20]+'    '+str(status.created_at))
            time.sleep(1)
            if len(tweet_list) == 100:
                self.disconnect()
                users_producer.close()
                tweets_producer.close()

        except Exception as e:
            print(e)

    def on_error(self, status):
        print(status)


real_time_stream = myStream(CONSUMER_KEY, CONSUMER_SECRET,
                            ACCESS_TOKEN, ACCESS_SECRET)
real_time_stream.sample()
