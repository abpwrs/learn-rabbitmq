import logging
from contextlib import contextmanager

import pika

logger = logging.getLogger(__name__)


@contextmanager
def connection_manager(host: str = "localhost"):
    try:
        logger.info("opening connection")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        yield connection
    finally:
        logger.info("closing connection")
        connection.close()
