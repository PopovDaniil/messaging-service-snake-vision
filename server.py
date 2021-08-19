#!/usr/bin/env python

# Receives messages from RabbitMQ and sends it to clients through WebSocket

import asyncio

import pika
import websockets

print('Starting RabbitMQ client...', end='', flush=True)
broker_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
broker_channel = broker_connection.channel()
broker_channel.queue_declare('control')
print('OK')

async def get_broker_message():
    return broker_channel.queue_declare(queue='control')

async def websocket_server(websocket, path):
    while True:
        message = (await get_broker_message())[2]

        if message: 
            print(f'[RabbitMQ] - Received: {message}')   
            await websocket.send(message)
            print(f"[WebSocket] - Sent: {message}")


print('Starting WebSocket server...', end='', flush=True)
start_server = websockets.serve(websocket_server, "localhost", 8765)
print('OK')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
