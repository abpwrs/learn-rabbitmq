#!/usr/bin/env python
import logging
import os
import sys

from src.connection_manager import connection_manager
from src.logging import configure, get_pid_file_logger

configure(logging.INFO)
logger = get_pid_file_logger("01")


def main():
    with connection_manager() as connection:
        channel = connection.channel()
        channel.queue_declare(queue="hello")

        def callback(ch, method, properties, body):
            logger.info("Received %r" % body)

        channel.basic_consume(
            queue="hello", on_message_callback=callback, auto_ack=True
        )

        logger.info("Waiting for messages")
        channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
