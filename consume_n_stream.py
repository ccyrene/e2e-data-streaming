import logging

from infrastructures.kafka import connect_to_kafka
from infrastructures.spark import create_spark_connection, select_df_from_kafka
from infrastructures.cassandra import create_cassandra_connection, create_keyspace, create_table

if __name__ == "__main__":
        
    spark_conn = create_spark_connection("localhost")

    if spark_conn is not None:
        spark_df = connect_to_kafka(spark_conn, "localhost:9092", "test_streaming")
        print(f"spark_df: {spark_df}")
        selected_df = select_df_from_kafka(spark_df)
        print(f"selected_df: {selected_df}")
        session = create_cassandra_connection("localhost")
        print(f"session: {session}")

        if session is not None:
            create_keyspace(session)
            print("HERE1")
            create_table(session)
            print("HERE2")

            streaming_query = (selected_df.writeStream.format("org.apache.spark.sql.cassandra")
                            .option('keyspace', 'spark_streams')
                            .option('table', 'test_streaming')
                            .option('checkpointLocation', '/tmp/spark-checkpoint')
                            .trigger(processingTime="10 seconds")
                            .start())
            
            print("HERE3")
            streaming_query.awaitTermination()


    # try:
    #     spark_conn = create_spark_connection("localhost")

    #     if spark_conn is not None:
    #         spark_df = connect_to_kafka(spark_conn, "localhost:9092", "test_streaming")
    #         print(f"spark_df: {spark_df}")
    #         selected_df = select_df_from_kafka(spark_df)
    #         print(f"selected_df: {selected_df}")
    #         session = create_cassandra_connection("localhost")
    #         print(f"session: {session}")

    #         if session is not None:
    #             create_keyspace(session)
    #             print("HERE1")
    #             create_table(session)
    #             print("HERE2")

    #             logging.info("Streaming is being started...")

    #             streaming_query = (selected_df.writeStream.format("org.apache.spark.sql.cassandra")
    #                             .option('checkpointLocation', '/tmp/checkpoint')
    #                             .option('keyspace', 'spark_streams')
    #                             .option('table', 'test_streaming')
    #                             .start())
                
    #             print("HERE3")

    #             streaming_query.awaitTermination()
                
    # except Exception as e:
    #     logging.error(f"Error: {e}")