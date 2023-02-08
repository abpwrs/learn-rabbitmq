#!/usr/bin/env python
import logging
import os
import time

from src.connection_manager import connection_manager
from src.logging import configure, get_pid_file_logger

configure(logging.INFO)
logger = get_pid_file_logger("02")

with connection_manager() as connection:
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)
    logger.info("Waiting for messages")

    def callback(ch, method, properties, body):
        logger.info(f"PID({os.getpid()}): received %r" % body.decode())
        time.sleep(body.count(b"."))
        logger.info(f"PID({os.getpid()}): done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="task_queue", on_message_callback=callback)

    channel.start_consuming()
