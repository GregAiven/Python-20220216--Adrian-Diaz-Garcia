from unittest.mock import call, patch

from monitor import settings
from monitor.__main__ import publish_results


@patch("kafka.KafkaProducer.send")
def test_publish_results(mock_kafka_producer):
    """
    test for publish_results checking that it publishes all the results received
    to the right topic.
    In this case the kafka producer is mocked as there is no need to test the library.
    """
    results = [
        {"http_status": 200, "check_result": True, "elapsed": 0.04, "regex": "fake", "url": "https://fakeurl"},
        {"http_status": 404, "check_result": True, "elapsed": 0.84, "regex": "fake", "url": "https://notfound"},
    ]
    publish_results(results=results)
    expected_calls = [call(settings.KAFKA_TOPIC, value=results[0]), call(settings.KAFKA_TOPIC, value=results[1])]
    mock_kafka_producer.assert_has_calls(expected_calls)
