import time
from json import dumps as json_dumps
from kafka import KafkaProducer


def run_producer(topic_name: str, server: str) -> bool:
    """
    :param topic_name: name of the kafka topic
    :param server: list of the kafka cluster's host:port
    :return: bool
    """
    try:
        producer_client = KafkaProducer(
            bootstrap_servers=server,
            value_serializer=lambda v: json_dumps(v).encode('utf-8')
        )
        how_many_names: int = int(input("How many names you want to enter... : "))
        print("Entering names...")
        for n in range(1, how_many_names+1):
            name: str = input(f"enter the {n} name : ")
            msg = {"name": name}
            partition: int = 0 if name[0] < "N" else 1
            print(f"{name} sending...")
            producer_client.send(topic_name, value=msg, partition=partition)
            time.sleep(0.2)
            print(f"{name} sent...")
        return True
    except Exception as e:
        print(e)
        return False


# producing data in kafka cluster
run_producer("users_info", "deepak-raj:9092")
