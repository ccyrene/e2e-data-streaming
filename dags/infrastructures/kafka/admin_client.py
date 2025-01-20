from kafka.admin import KafkaAdminClient

def get_admin_client(config):
    return KafkaAdminClient(**config)