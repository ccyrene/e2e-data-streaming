import os 

from .airflow import AirflowConfig
from .kafka import KafkaConfig

from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def load_config():
    return {config_name: _load_config(config_name) for config_name in ["airflow", "kafka"]}

def _load_config(config):
    match config:
        case "airflow":
            cfg = AirflowConfig(
                owner=os.getenv("AIRFLOW_OWNER", "himari"),
                start_date=datetime.now(),
            )

        case "kafka":
            cfg = KafkaConfig(
                bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"),
                max_block_ms=int(os.getenv("KAFKA_MAX_BLOCK_MS", 1000)),
            )

    return cfg.to_dict()