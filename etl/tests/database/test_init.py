from datetime import datetime


def test_insert_all(setup_db, db_client):
    data_to_insert = [
        {"http_status": 200, "check_result": True, "elapsed": 0.04, "regex": "fake", "url": "https://fakeurl"},
        {"http_status": 404, "check_result": True, "elapsed": 0.84, "regex": "fake", "url": "https://notfound"},
    ]
    with db_client.client.cursor() as curs:
        curs.execute("SELECT * FROM check_results;")
        results = curs.fetchall()
        assert results == []  # Asserting database is empty at this stage

        db_client.insert_all(data_to_insert)
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
