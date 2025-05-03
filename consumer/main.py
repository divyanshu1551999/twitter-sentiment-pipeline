from kafka import KafkaConsumer
from textblob import TextBlob
import json
from google.cloud import bigquery

# Kafka setup
consumer = KafkaConsumer(
    'twitter-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# BigQuery client
bq_client = bigquery.Client()
table_id = 'your_project.your_dataset.twitter_sentiment'

# Process and send to BigQuery
for msg in consumer:
    tweet = msg.value
    analysis = TextBlob(tweet['text'])
    sentiment = analysis.sentiment.polarity

    row = {
        'tweet_id': tweet['id'],
        'text': tweet['text'],
        'sentiment': sentiment
    }

    bq_client.insert_rows_json(table_id, [row])
