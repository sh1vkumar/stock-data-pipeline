from kafka import KafkaConsumer
import json
from dotenv import load_dotenv
import os

load_dotenv()


consumer = KafkaConsumer(
    os.getenv("KAFKA_TOPIC"),
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    group_id='stock-consumer-group',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: x.decode('utf-8')  # Just decode bytes, not JSON yet
)

print("Listening for messages...")

for message in consumer:
    try:
        data = json.loads(message.value)
        print(f"✅ Received: {data}")
    except json.JSONDecodeError as e:
        print(f"❌ JSONDecodeError: {e} | Raw: {message.value}")