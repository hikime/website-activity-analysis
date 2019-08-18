import json
from kafka import KafkaConsumer


class Consumer:
    bootstrap_servers = '127.0.0.1:9092'
    topic = 'flask'

    def listen(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092', value_deserializer=lambda v: json.loads(v).encode('utf-8'), consumer_timeout_ms=10000)
        consumer.subscribe([self.topic])
        for message in consumer:
            pass
