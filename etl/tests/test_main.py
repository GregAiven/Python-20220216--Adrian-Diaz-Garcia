import collections
from datetime import datetime
from unittest.mock import patch

import pytest

from etl.__main__ import consume_results, run

# Mocking message kafka consumer message using a namedtuple
KakfaMessage = collections.namedtuple("Message", "value")


@patch("kafka.KafkaConsumer.poll")
def test_consume_results(mock_kafka_consumer):
    """
    Testing how consume results is consuming messages from kafka
    and how are those returned by the function.
    As well making sure the timeout_ms is passed to the poll function.
    """
    mock_kafka_consumer.return_value = {
        "Topic": [
            KakfaMessage(
                {"http_status": 200, "check_result": True, "elapsed": 0.04, "regex": "fake", "url": "https://fakeurl"}
            ),
            KakfaMessage(
                {"http_status": 404, "check_result": True, "elapsed": 0.84, "regex": "fake", "url": "https://notfound"}
            ),
        ]
    }
    results = consume_results()
    mock_kafka_consumer.assert_called_with(timeout_ms=500)

    assert results[0]["http_status"] == 200
    assert results[0]["check_result"] is True
    assert results[0]["elapsed"] == 0.04
    assert results[0]["regex"] == "fake"
    assert results[0]["url"] == "https://fakeurl"

    assert results[1]["http_status"] == 404
    assert results[1]["check_result"] is True
    assert results[1]["elapsed"] == 0.84
    assert results[1]["regex"] == "fake"
    assert results[1]["url"] == "https://notfound"


@patch("kafka.KafkaConsumer.poll")
def test_run(mock_kafka_consumer, setup_db, db_client):
    """
    Testing the run method where both functions (insde_all) and consumer_results
    are glued together
    """

    def consume_results_side_effect(*args, **kwargs):
        """
        Configuring the side_effect for the mock so first it yields a response
        and later on raises an InterruptedError exception
        """
        yield {
            "Topic": [
                KakfaMessage(
                    {
                        "http_status": 200,
                        "check_result": True,
                        "elapsed": 0.04,
                        "regex": "fake",
                        "url": "https://fakeurl",
                    }
                ),
                KakfaMessage(
                    {
                        "http_status": 404,
                        "check_result": True,
                        "elapsed": 0.84,
                        "regex": "fake",
                        "url": "https://notfound",
                    }
                ),
            ]
        }
        yield InterruptedError

    mock_kafka_consumer.side_effect = consume_results_side_effect()

    with db_client.client.cursor() as curs:
        curs.execute("SELECT * FROM check_results;")
        results = curs.fetchall()
        assert results == []  # Asserting database is empty at this stage

        with pytest.raises(InterruptedError):  # Consume_results will raise it to stop run execution
            run()  # Call run method (main entrypoint for the etl process)

            curs.execute("SELECT * FROM check_results order by id asc;")
            results = curs.fetchall()

            assert results[0][0] == 1  # id
            assert results[0][1] == "https://fakeurl"  # url
            assert results[0][2] == "fake"  # pattern
            assert results[0][3] == 200  # http_status
            assert results[0][4] is True  # check_status
            assert results[0][5] == 0.04  # elapsed
            assert isinstance(results[0][6], datetime)  # checking date field is datetime

            assert results[1][0] == 2  # id
            assert results[1][1] == "https://notfound"  # url
            assert results[1][2] == "fake"  # pattern
            assert results[1][3] == 404  # http_status
            assert results[1][4] is True  # check_status
            assert results[1][5] == 0.84  # elapsed
            assert isinstance(results[1][6], datetime)  # checking date field is datetime
