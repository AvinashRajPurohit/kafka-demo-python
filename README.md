# kafka-demo-python

```
A simple demo for kafka using python
```

Built with ❤︎ and :coffee: [Deepak Rajpurohit](https://github.com/AvinashRajPurohit)

---

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) 


# Explaination
#### Basic Concept:
- docker
- kafka
- python
- vim


# Setup

### zookeeper - kafka setup using docker
Note: Docker and docker compose should be installed in your system.

```bash
git clone https://github.com/wurstmeister/kafka-docker.git 
cd kafka-docker/
touch docker-compose-expose.yml
vim docker-compose-expose.yml
```


Now paste this code in the file.


```bash
version: '2'
services:
  zookeeper:
    image: wurstmeister/zookeeper:3.4.6
    ports:
     - "2181:2181"
  kafka:
    image: wurstmeister/kafka
    ports:
     - "9092:9092"
    expose:
     - "9093"
    environment:
      KAFKA_ADVERTISED_LISTENERS: INSIDE://kafka:9093,OUTSIDE://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INSIDE:PLAINTEXT,OUTSIDE:PLAINTEXT
      KAFKA_LISTENERS: INSIDE://0.0.0.0:9093,OUTSIDE://0.0.0.0:9092
      KAFKA_INTER_BROKER_LISTENER_NAME: INSIDE
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
    volumes:
     - /var/run/docker.sock:/var/run/docker.sock
```


Now run up the the file using below command

```bash
sudo docker-compose -f docker-compose-expose.yml up
```

```bash
git clone https://github.com/AvinashRajPurohit/kafka-demo-python.git
cd kafka-demo-python
pip install -r requirements.txt
```

### References.
[Youtube Hussein Nasser (Good Tuts..)](https://youtube.com/channel/UC_ML5xP23TOWKUcc-oAE_Eg) <br>
[Medium blog by Shuyi Yang](https://towardsdatascience.com/kafka-docker-python-408baf0e1088) <br>
[Python Kafka Docs](https://kafka-python.readthedocs.io/en/master/) <br>

## Thank you and Happy Learning