import logging

from cassandra.cluster import Cluster

def create_cassandra_connection(url: str):
    cas_session = None
    try:
        cluster = Cluster(contact_points=[url])
        cas_session = cluster.connect()
        logging.info("connect to Cassandra is successfully")
    except Exception as e:
        logging.error(f"Could not create cassandra connection due to {e}")
    
    return cas_session