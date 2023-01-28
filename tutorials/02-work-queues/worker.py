#!/usr/bin/env python
import os
import time
from src.connection_manager import connection_manager


with connection_manager() as connection:
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)
    print(" [*] Waiting for messages. To exit press CTRL+C")

    def callback(ch, method, properties, body):
        print(f" [x] PID({os.getpid()}): received %r" % body.decode())
        time.sleep(body.count(b"."))
        print(f" [x] PID({os.getpid()}): done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="task_queue", on_message_callback=callback)

    channel.start_consuming()
