# End to End Data Streaming from Data source API to Cassandra

This repository contains the implementation of a scalable, real-time data processing and orchestration system. The architecture is designed for handling streaming data efficiently and leveraging modern tools for data processing, orchestration, and storage.

---

## System Overview
![System Overview](https://raw.githubusercontent.com/ccyrene/e2e-data-streaming/main/diagram.svg)


The architecture comprises the following components:

### 1. **API**
   - Serves as the entry point for data ingestion.
   - Processes incoming requests and forwards data to the streaming pipeline.

### 2. **Apache Airflow**
   - Responsible for orchestrating workflows.
   - Connects to a PostgreSQL database for managing metadata and task execution.

### 3. **Apache Kafka**
   - Acts as the central streaming platform.
   - Handles real-time data streams and integrates with:
     - **Control Center**: For monitoring Kafka metrics.
     - **Schema Registry**: For managing data schemas.

### 4. **Apache ZooKeeper**
   - Provides distributed coordination for Kafka.

### 5. **Apache Spark**
   - Handles distributed data processing.
   - Includes a Spark master node and multiple worker nodes to process streams from Kafka.

### 6. **Cassandra**
   - Serves as the distributed database for storing processed data.

### 7. **Docker**
   - Used for containerizing all components.
   - Ensures consistency and portability across environments.

---

## System Flow

1. **Data Ingestion**:
   - Data is ingested through the API and forwarded to Apache Kafka.

2. **Workflow Orchestration**:
   - Apache Airflow schedules and manages tasks for processing the data streams.

3. **Streaming and Processing**:
   - Apache Kafka handles real-time data streams and integrates with the schema registry for data validation.
   - Apache Spark processes the streaming data in parallel across its cluster (master and workers).

4. **Data Storage**:
   - The processed data is stored in Cassandra for fast and reliable access.

---

## Prerequisites

To run the system, ensure you have the following installed:

- Docker and Docker Compose
- Python 3.8+
- Apache Airflow
- Apache Kafka
- Apache Spark
- Cassandra

.env file
```bash
KAFKA_BOOTSTRAP_SERVERS=broker:29092
KAFKA_MAX_BLOCK_MS=5000

AIRFLOW_OWNER=YOUR_NAME

DATASOURCE_URL=https://randomuser.me/api/
```

---

## Setup and Deployment

1. Clone this repository:
   ```bash
   git clone https://github.com/ccyrene/e2e-data-streaming
   cd e2e-data-streaming
   ```

2. Start the Docker containers:
   ```bash
   docker-compose up -d
   ```

3. Verify the components are running:
   - Access Apache Kafka Control Center at `http://localhost:9021`
   - Check Airflow's web interface at `http://localhost:8080`

4. Trigger workflows and monitor data processing in Airflow.

5. Consume data from Kafka and streaming to Cassandra.
    - local
    ```bash
    python consume_n_stream.py 
    ``` 
    or
    ```bash
    spark-submit  \
    --master local["*"]  \
    --conf spark.cassandra.connection.host=localhost  \
    --packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
    consume_n_stream.py
    ```
    - cluster
    ```bash
    spark-submit  \
    --master spark://localhost:7077  \
    --conf spark.cassandra.connection.host=localhost  \
    --packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
    consume_n_stream.py
    ```
---

## Monitoring and Maintenance

- Monitor Kafka and Spark metrics using the Control Center.
- Review Airflow DAG execution status and logs in its web interface.
- Scale Spark workers by adjusting the configuration in `docker-compose.yml`

---

## License

This project is licensed under the [MIT License](LICENSE)