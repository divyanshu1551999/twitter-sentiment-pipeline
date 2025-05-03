import tweepy
from kafka import KafkaProducer
import json

# Twitter API credentials (use your own)
bearer_token = 'YOUR_TWITTER_BEARER_TOKEN'

# Kafka setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Tweepy Streaming Client
class TweetStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if tweet.lang == 'en':
            producer.send('twitter-topic', {'id': tweet.id, 'text': tweet.text})

# Start stream
stream = TweetStream(bearer_token)
stream.add_rules(tweepy.StreamRule("data OR AI OR cloud"))
stream.filter(tweet_fields=["lang"])
