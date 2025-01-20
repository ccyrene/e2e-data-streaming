import os
import json

from dotenv import load_dotenv
from airflow import DAG
from airflow.operators.python import PythonOperator

from config import load_config
from infrastructures import get_producer

from streaming import streaming

load_dotenv()

cfg = load_config()

op_kwargs = {
    "url": os.getenv("DATASOURCE_URL"),
    "producer_config": cfg["kafka"],
    "topic": "test_streaming",
    "timeout": 60,
}

with DAG('user_automation',
         default_args=cfg["airflow"],
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=streaming,
        op_kwargs=op_kwargs,
    )