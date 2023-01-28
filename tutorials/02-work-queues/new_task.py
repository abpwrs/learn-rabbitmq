#!/usr/bin/env python
import pika
import sys

from src.connection_manager import connection_manager

with connection_manager() as connection:

    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    message = " ".join(sys.argv[1:]) or "Hello World! ..."
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ),
    )
    print(" [x] Sent %r" % message)
