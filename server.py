#!/usr/bin/env python

# Receives messages from RabbitMQ and sends it to clients through WebSocket

import asyncio

import pika
import websockets


async def rabbitmq_client():
    print('Starting RabbitMQ client...', end='', flush=True)
    broker_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    broker_channel = broker_connection.channel()
    broker_channel.queue_declare('control')
    print('OK')
    
    while True:
        mes = broker_channel.basic_get(queue='control', auto_ack=True)
        if mes[2]:
            print(mes)

async def websocket_server():
    async def on_receive(websocket, path):
        while True:
            message = (await rabbitmq_client())[2]

            if message: 
                print(f'[RabbitMQ] - Received: {message}')   
                await websocket.send(message)
                print(f"[WebSocket] - Sent: {message}")

    print('Starting WebSocket server...', end='', flush=True)
    websockets.serve(on_receive, "localhost", 8765)
    print('OK')

async def main():
    await asyncio.to_thread(rabbitmq_client)
    await asyncio.to_thread(websocket_server)

asyncio.run(main())
