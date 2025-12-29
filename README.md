# Goal
The goal of this project is to develop a small realistic real-time data pipeline including steps ingestion -> streaming processing -> storage -> consumption.

Technologies used:
1. Kafka
2. Spark Structured Streaming
3. Delta lake storage
4. Dashboard

## Requirements
1. Data Producer (FastAPI)
   Service that generates JSON events and pushes them into Kafka continuosly.
2. Kafka Cluster
3. Spark Structured Streaming
4. Storage Layer
5. Dashboard using Streamlit.

### How to Run
1. Install uv - https://docs.astral.sh/uv/getting-started/installation/
2. Run `uv sync`
3. Run `docker compose up -d` to set up local spark and kafka docker images.
4. To run the server - `uv run fastapi run ./api/app.py`
5. To generate random events: `curl localhost:8000/generate_event` or do a get request to call `localhost:8000/generate_event`
6. `docker compose down -v` to stop the containers and delete the volumes created.