import json
from kafka import KafkaConsumer


class Consumer:
    bootstrap_servers = '127.0.0.1:9092'
    topic = 'flask'

    def listen(self):
        consumer = KafkaConsumer(self.bootstrap_servers, value_serializer=lambda v: json.loads(v).encode('utf-8'))
        consumer.subscribe([self.topic])

        for message in consumer:
            print(message)
