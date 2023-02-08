#!/usr/bin/env python
import logging

from src.connection_manager import connection_manager
from src.logging import configure, get_pid_file_logger

configure(logging.INFO)
logger = get_pid_file_logger("01")

with connection_manager() as connection:
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange="", routing_key="hello", body="Hello There!")
    logger.info("Sent 'Hello World!'")
