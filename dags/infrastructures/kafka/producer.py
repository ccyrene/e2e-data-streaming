from kafka import KafkaProducer

def get_producer(config):
    return KafkaProducer(**config)