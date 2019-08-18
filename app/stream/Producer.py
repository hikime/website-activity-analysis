import json
from kafka import KafkaProducer


class Producer:
    # bootstrap_servers = '127.0.0.1:9092'
    # acks = 1
    # compression_type = 'gzip'
    # key_serializer = str.encode('utf-8')

    def sending(self):
        # pass
        producer= KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send('flask', {'key': 'flask-kafka'})
        # used for dev purpose
        producer.flush()
