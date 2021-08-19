import sys
import pika

message = sys.argv[1]
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare('control')
channel.basic_publish(exchange='',
                      routing_key='control',
                      body=message)
print("Sent %r" % message)