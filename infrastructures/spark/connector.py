import logging

from pyspark.sql import SparkSession

def create_spark_connection(url: str):
    s_conn = None
    
    try:
        s_conn = SparkSession.builder \
                .appName('SparkDataStreaming') \
                .config('spark.jars.packages', 
                        "com.datastax.spark:spark-cassandra-connector_2.12:3.5.1,"
                        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1") \
                .config("spark.sql.extensions", "com.datastax.spark.connector.CassandraSparkExtensions") \
                .config('spark.cassandra.connection.host', url) \
                .config("spark.cassandra.connection.port", "9042") \
                .getOrCreate()

        s_conn.sparkContext.setLogLevel("ERROR")
        logging.info("Spark connection created successfully!")
    except Exception as e:
        logging.error(f"Couldn't create the spark session due to exception {e}")

    return s_conn