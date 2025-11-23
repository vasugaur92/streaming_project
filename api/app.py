from fastapi import FastAPI

from kafka import KafkaProducer, KafkaConsumer
from faker import Faker
import json

app = FastAPI()

fake = Faker()


@app.get("/generate_event")
def generate_event():
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        acks="all",
    )
    event_json = {
        "name": fake.name(),
        "location": fake.city(),
        "customer_id": fake.random_number(digits=5),
        "order_id": fake.random_number(digits=7),
        "amount": fake.random_number(digits=3),
        "timestamp": fake.iso8601(),
    }
    producer.send("events_topic", event_json)
    producer.flush()

    return event_json


@app.get("/read_event")
def read_event():
    consumer = KafkaConsumer(
        "events_topic",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="my-group",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        consumer_timeout_ms=1000,
    )
    messages = []
    for message in consumer:
        messages.append(message.value)
    return {"messages": messages}
