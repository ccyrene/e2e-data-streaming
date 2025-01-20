#!/bin/bash
set -e

# Upgrade pip and install requirements if they exist
if [ -e "/opt/airflow/requirements.txt" ]; then
  echo "Upgrading pip and installing requirements..."
  python -m pip install --upgrade pip
  pip install -r /opt/airflow/requirements.txt
fi

# Initialize the Airflow database if it hasn't been initialized
if [ ! -f "/opt/airflow/airflow.db" ]; then
  echo "Initializing Airflow database..."
  airflow db init
  echo "Creating default admin user..."
  airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin
fi

# Apply database migrations
echo "Upgrading Airflow database..."
airflow db upgrade

# Start the webserver
echo "Starting Airflow webserver..."
exec airflow webserver
