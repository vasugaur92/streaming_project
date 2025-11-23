from fastapi import FastAPI

# from kafka import KafkaProducer
from faker import Faker

app = FastAPI()

fake = Faker()


@app.get("/generate_event")
def generate_event():
    # producer = KafkaProducer(bootstrap_servers=["host.docker.internal:9092"])
    event_json = {
        "name": fake.name(),
        "location": fake.city(),
        "customer_id": fake.random_number(digits=5),
        "order_id": fake.random_number(digits=7),
        "amount": fake.random_number(digits=3),
    }

    return event_json
