import time
import json
import logging

from utils import get_data
from transforms import format_data

from infrastructures.kafka import get_producer, get_admin_client, topic_exists, create_topic

def streaming(url, producer_config, topic, timeout=30):
    
    admin_client_config = {"bootstrap_servers": producer_config["bootstrap_servers"]}
    
    producer = get_producer(producer_config)
    admin_client = get_admin_client(admin_client_config)
    
    current_time = time.time()
    try:
        while True:
            if time.time() > current_time + timeout:
                break
            
            try:
                data = get_data(url)
                formatted_data = format_data(data)
                if not topic_exists(admin_client, topic):
                    create_topic(admin_client, topic)
                    
                producer.send(topic, json.dumps(formatted_data).encode('utf-8'))
                
                logging.info("Data sent to Kafka.")
                
            except Exception as e:
                logging.error(f'An error occurred: {e}')
                continue
                
    finally:
        logging.info("Finally close producer & admin_client.")
        producer.close()
        admin_client.close()