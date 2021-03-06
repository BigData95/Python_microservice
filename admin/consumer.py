import json
import os

import django
import pika

from products.models import Product

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()


# Use https://www.cloudamqp.com/
params = pika.URLParameters(os.getenv('CLOUD_AMQP'))

connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)

print("started consuming")

channel.start_consuming()
channel.close()
