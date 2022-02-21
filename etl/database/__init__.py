import logging

import psycopg2

from etl import settings

SQL_INSERT_QUERY = """INSERT INTO check_results (url, regex, http_status, check_result, elapsed)
                   VALUES (%(url)s,%(regex)s,%(http_status)s,%(check_result)s,%(elapsed)s) """


class DB:
    def __init__(self):
        try:
            self.client = psycopg2.connect(
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                database=settings.DB_DATABASE,
            )

        except (Exception, psycopg2.Error):
            logging.exception("Error while connecting to PostgreSQL")

    def insert_all(self, entries):
        try:
            with self.client.cursor() as curs:
                curs.executemany(SQL_INSERT_QUERY, entries)
                self.client.commit()
        except psycopg2.InterfaceError:
            logging.exception("Error while inserting entries in the database")
