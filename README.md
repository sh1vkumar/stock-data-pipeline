# 📈 Real-Time Stock Data Pipeline with Kafka, Python, and MongoDB

This project fetches real-time stock data using the [Finnhub API](https://finnhub.io/), streams it using **Apache Kafka**, and stores it in **MongoDB** for further analysis or processing. Kafka is deployed using **Docker**, and all ingestion and processing logic is written in **Python**.

---

## 🚀 Features

- Live stock market data streaming using WebSocket
- Kafka-based data ingestion pipeline
- Docker-based Kafka broker setup
- Python-based producer and consumer services
- Data storage in MongoDB

---

## 🗂️ Project Structure
│
├── docker-compose.yml             # Kafka, Zookeeper, MongoDB services
├── kafka/
│   └── create_topic.sh            # Script to create Kafka topic
│
├── producer/
│   ├── producer.py                # Connects to Finnhub WebSocket and produces to Kafka
│   └── .env                       # API key and bootstrap server details
│
├── consumer/
│   └── consumer_kafka_mongo.py    # Consumes from Kafka and inserts into MongoDB
│
├── requirements.txt               # Python dependencies
└── README.md                      # You are here

---

## 🐳 Docker Setup for Kafka & MongoDB

### Step 1: Start Kafka and MongoDB

```bash
docker-compose up -d

docker exec -it kafka /bin/bash
cd /opt/kafka/bin
./kafka-topics.sh --create --topic stock-data --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

📬 Sample Output

Producer:
Produced: {'type': 'trade', 'data': [{'p': 134.5, 's': 'AAPL', ...}]}

Consumer:
✔ Received: {'type': 'trade', 'data': [...]} → Inserted into MongoDB

```
---

🙌 Acknowledgements
    •   Finnhub.io
	•	Apache Kafka
	•	MongoDB