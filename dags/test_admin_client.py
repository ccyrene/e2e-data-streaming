from kafka.admin import KafkaAdminClient

config = {
    "bootstrap_servers": "localhost:9092",
}

admin_client = KafkaAdminClient(**config)