import logging

from infrastructures.kafka import connect_to_kafka
from infrastructures.spark import create_spark_connection, select_df_from_kafka
from infrastructures.cassandra import create_cassandra_connection, create_keyspace, create_table

if __name__ == "__main__":

    try:
        spark_conn = create_spark_connection("localhost")

        if spark_conn is not None:
            spark_df = connect_to_kafka(spark_conn, "localhost:9092", "test_streaming")
            selected_df = select_df_from_kafka(spark_df)
            session = create_cassandra_connection("localhost")

            if session is not None:
                create_keyspace(session)
                create_table(session)

                logging.info("Streaming is being started...")

                streaming_query = (selected_df.writeStream.format("org.apache.spark.sql.cassandra")
                                .option('checkpointLocation', '/tmp/checkpoint')
                                .option('keyspace', 'spark_streams')
                                .option('table', 'test_streaming')
                                .start())

                streaming_query.awaitTermination()
                
    except Exception as e:
        logging.error(f"Error: {e}")