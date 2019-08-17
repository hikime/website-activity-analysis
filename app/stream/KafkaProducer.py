import json
from kafka import KafkaProducer


class Producer:
    bootstrap_servers = '127.0.0.1:9092'
    acks = 1
    compression_type = 'gzip'
    key_serializer = str.encode()

    def send(self):
        producer= KafkaProducer(self.bootstrap_servers, self.acks, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send('flask', {'key': 'flask-kafka'})
