import websocket
from dotenv import load_dotenv
import os
import ssl
import certifi
from kafka import KafkaProducer
import json

load_dotenv()

FINNHUB_TOKEN = os.getenv("FINNHUB_TOKEN")

producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    value_serializer=lambda x: json.dumps(x).encode('utf-8'),  # ✅ valid JSON
    key_serializer=lambda x: str(x).encode('utf-8')  # key can stay as string
)

def on_message(ws, message):
    try:
        json_data = json.loads(message)  # Ensure it's valid JSON
        producer.send(os.getenv("KAFKA_TOPIC"), value=json_data)
        print(f"✅ Produced: {json_data}")
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}, raw message: {message}")
    except Exception as e:
        print(f"❌ Kafka send error: {e}")

def on_error(ws, error):
    print("❌ Error:", error)

def on_close(ws, close_status_code, close_msg):
    print(f"Connection closed ; code={close_status_code}, reason={close_msg}")

def on_open(ws):
    # ws.send('{"type":"subscribe","symbol":"AAPL"}')
    # ws.send('{"type":"subscribe","symbol":"AMZN"}')
    # ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        f"wss://ws.finnhub.io?token={FINNHUB_TOKEN}",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_REQUIRED, "ca_certs": certifi.where()})