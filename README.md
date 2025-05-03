# 📊 Real-Time Twitter Sentiment Analysis Pipeline

A real-time data pipeline that streams tweets from Twitter using Kafka, analyzes sentiment using NLP, and stores results in Google BigQuery for visualization in Looker Studio. Deployed using Docker and Google Cloud Run.

---

## 🛠️ Technologies Used

- **Python** – Data processing and sentiment analysis
- **Apache Kafka** – Real-time streaming platform
- **Google BigQuery** – Scalable data warehouse
- **Google Looker Studio** – Real-time visualization dashboard
- **Google Cloud Run** – Serverless deployment
- **Docker** – Containerization

---

## 📁 Project Structure
twitter-sentiment-pipeline/
│
├── producer/ # Twitter stream producer
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── consumer/ # Kafka consumer + sentiment analysis
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── .gitignore
├── .dockerignore
└── README.md



---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/divyanshu1551999/twitter-sentiment-pipeline.git
cd twitter-sentiment-pipeline

2. Kafka Setup (Local)
You can use Docker Compose or a Confluent Cloud Kafka cluster.

Example local Kafka via Docker:

bash:

docker run -d --name kafka \
  -p 9092:9092 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  confluentinc/cp-kafka


3. Producer (Twitter → Kafka)
Update producer/main.py with your Twitter API bearer token.

bash:

cd producer
docker build -t twitter-producer .
docker run --network="host" twitter-producer

4. Consumer (Kafka → BigQuery)
Update your GCP BigQuery table ID and make sure your GCP credentials are available.

bash:

cd consumer
docker build -t twitter-consumer .
docker run --network="host" \
  -e GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json \
  twitter-consumer

5. Cloud Run Deployment
Use these commands to deploy each component:

gcloud builds submit --tag gcr.io/YOUR_PROJECT/twitter-producer
gcloud builds submit --tag gcr.io/YOUR_PROJECT/twitter-consumer

gcloud run deploy twitter-producer \
  --image gcr.io/YOUR_PROJECT/twitter-producer \
  --platform managed --region us-central1 --allow-unauthenticated

gcloud run deploy twitter-consumer \
  --image gcr.io/YOUR_PROJECT/twitter-consumer \
  --platform managed --region us-central1 --allow-unauthenticated


📊 Visualization with Looker Studio
1. Connect Looker Studio to your BigQuery dataset.

2. Create charts using the sentiment column over time.

3. Publish and share the dashboard with stakeholders.
