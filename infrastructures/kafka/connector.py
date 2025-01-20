import logging

def connect_to_kafka(spark_conn, bootstrap_servers, topic):
    
    spark_df = None
    try:
        spark_df = spark_conn.readStream \
            .format('kafka') \
            .option('kafka.bootstrap.servers', bootstrap_servers) \
            .option('subscribe', topic) \
            .option('startingOffsets', 'earliest') \
            .load()
            
        logging.info("kafka dataframe created successfully")
    except Exception as e:
        logging.warning(f"kafka dataframe could not be created because: {e}")

    return spark_df