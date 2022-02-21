import asyncio
import logging
import time
from json import dumps
from typing import Dict, List

from kafka import KafkaProducer

from monitor import settings
from monitor.crawler import check_all

logging.basicConfig(level=settings.LOG_LEVEL)

producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVER,
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)


def gather_web_results() -> List[Dict]:
    """
    schedule the requests for each website defined in settings and await for the
    results to come back
    :return: List with results for each check
    :rtype: List[Dict]
    """
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(check_all())
    return results


def publish_results(results: List[Dict]):
    """
    Publish results to kafka topic
    :param results: Results from the web checks
    :type results:  List[Dict]
    """

    for result in results:
        logging.info("Publishing message to kafka topic %s", settings.KAFKA_TOPIC)
        logging.debug("message: %s", result)
        producer.send(settings.KAFKA_TOPIC, value=result)

    producer.flush()  # Wait until all messages are sent


def run():
    for i in range(100):
        publish_results(gather_web_results())
        time.sleep(5)  # Sleep 5 secs to avoid ddosing the websites


if __name__ == "__main__":
    run()
