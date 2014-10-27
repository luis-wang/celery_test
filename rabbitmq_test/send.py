#!/usr/bin/env python
import pika

host = '115.29.185.223' # 'localhost'

connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World! this is from send.py')
print " [x] Sent 'Hello World!'"

connection.close()

