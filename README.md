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