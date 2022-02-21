import logging
import os
import subprocess

import pytest

from etl.database import DB


@pytest.fixture()
def setup_db(db_client):
    # Making use of the script to initdb
    # TODO: Consider if that's the best way to do that
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "initdb.sh")
    subprocess.run(path, shell=True, check=True)
    logging.info("database provisioned")

    # TODO: This will prune local database, probably that's ok for this kind of project
    # consider making use of a separate database when running tests
    with db_client.client.cursor() as curs:
        # RESTART IDENTITY is used to restart the id Sequence
        curs.execute("TRUNCATE table check_results RESTART IDENTITY;")
        db_client.client.commit()


@pytest.fixture()
def db_client():
    yield DB()
