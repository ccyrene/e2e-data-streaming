import logging
from kafka.admin import NewTopic

def topic_exists(admin_client, topic_name):
    try:
        existing_topics = admin_client.list_topics()
        return topic_name in existing_topics
    except Exception as e:
        logging.error(f"Failed to check or create topic '{topic_name}': {e}")
        
def create_topic(admin_client, topic_name, partitions=1, replication_factor=1):
    try:
        topic = NewTopic(name=topic_name, num_partitions=partitions, replication_factor=replication_factor)
        admin_client.create_topics([topic])
        
        logging.info(f"Topic '{topic_name}' created successfully.")
    except Exception as e:
        logging.error(f"Failed to check or create topic '{topic_name}': {e}")