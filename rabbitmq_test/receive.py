#!/usr/bin/env python
import pika

host = '115.29.185.223' # 'localhost'

connection = pika.BlockingConnection(pika.ConnectionParameters(host))
channel = connection.channel()


channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()


