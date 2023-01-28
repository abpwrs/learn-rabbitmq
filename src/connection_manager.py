import pika
from contextlib import contextmanager


@contextmanager
def connection_manager(host: str = "localhost"):
    try:
        print("opening connection")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        yield connection
    finally:
        print("closing connection")
        connection.close()
