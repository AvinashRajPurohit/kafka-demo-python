from kafka import KafkaConsumer
from json import loads as json_loads
from time import sleep


def run_consumer(topic_name: str, server: str) -> bool:
    """
    :param topic_name: name of the kafka topic
    :param server: list of the kafka cluster's host:port
    :return: bool
    """
    try:
        consumer = KafkaConsumer(
            topic_name,
            bootstrap_servers=server,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json_loads(x.decode('utf-8'))
        )
        print("Consuming names...")
        for event in consumer:
            event_data = event.value
            print("consumed, ", event_data)
            sleep(0.2)
        consumer.close()
        return True
    except Exception as e:
        print(e)
        return False


# consuming data in kafka cluster
run_consumer("users_info", "deepak-raj:9092")
