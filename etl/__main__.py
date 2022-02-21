import logging
from json import loads

from kafka import KafkaConsumer

from etl import settings
from etl.database import DB

logging.basicConfig(level=settings.LOG_LEVEL)

consumer = KafkaConsumer(
    settings.KAFKA_TOPIC,
    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id=settings.KAFKA_GROUP_ID,
    value_deserializer=lambda x: loads(x.decode("utf-8")),
    max_poll_records=settings.KAFKA_BATCH_SIZE,  # Consuming in batch to make better insertions in the database
)

database = DB()


def consume_results():
    """
    Consume results timing out on 500 ms
    Messages are consumed in batches, so they can be added in batches to postgresql
    Adding several entries at once give us the ability to improve the performance
    and reduce the number of queries issued to the database.
    :return: List of messages already prepared to be added to the db.
    :rtype: List
    """
    for topicpartition, messages in consumer.poll(timeout_ms=500).items():
        logging.debug("Message consumed from kafka %s", messages)
        return [msg.value for msg in messages]


def run():
    """
    Entrypoint for the etl to work, it will be looping indefinetlly until an Interruption is sent
    consuming every single possible message from Kafka
    """
    while True:
        try:
            results = consume_results()
            if results:
                # Store them in the database
                database.insert_all(results)
        except InterruptedError as e:
            logging.info("Got interrupted, shutting down...")
            raise e
        except Exception as e:
            logging.exception("could not read from kafka: {}".format(str(e)))
            raise e


if __name__ == "__main__":
    run()
