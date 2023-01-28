#!/usr/bin/env python
from src.connection_manager import connection_manager

with connection_manager() as connection:
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange="", routing_key="hello", body="Hello There!")
    print(" [x] Sent 'Hello World!'")
