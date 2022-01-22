from kafka.admin import KafkaAdminClient, NewTopic


def create_kafka_topic(topic_name: str, server: str, client_id: str) -> bool:
    """
    :param topic_name: name of the kafka topic
    :param server: list of the kafka cluster's host:port
    :param client_id: name of the client
    :return: bool
    """
    try:
        admin_client = KafkaAdminClient(
            bootstrap_servers=server,
            client_id=client_id,
            api_version=(0, 1, 0)
        )
        topic_list = [NewTopic(name=topic_name, num_partitions=2, replication_factor=1)]
        print("Creating...")
        created_topics = admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print("Created...")
        print(created_topics)
        return True
    except Exception as e:
        print(e)
        return False


# creating users topic
create_kafka_topic("users_info", "deepak-raj:9092", 'test-app')
