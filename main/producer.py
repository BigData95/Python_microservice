import json
import os

import pika

# Use https://www.cloudamqp.com/ 
params = pika.URLParameters(os.getenv('CLOUD_AMQP'))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    print('Sending')
    channel.basic_publish(exchange='', routing_key='admin',
                          body=json.dumps(body), properties=properties)
