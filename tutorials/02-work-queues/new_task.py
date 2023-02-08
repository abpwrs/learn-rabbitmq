#!/usr/bin/env python
import logging
import sys

import pika

from src.connection_manager import connection_manager
from src.logging import configure, get_pid_file_logger

configure(logging.INFO)
logger = get_pid_file_logger("02")

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
    logger.info("Sent %r" % message)
