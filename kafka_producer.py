
from kafka import KafkaProducer
import csv
import json
import time
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'mytopic'


with open('telecom_churn.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        json_data = json.dumps(row).encode('utf-8')
        producer.send(topic, value=json_data)

