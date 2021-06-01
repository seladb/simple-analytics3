import logging
from random import randint
from time import sleep
from common.record import Record


class DBService:
    def write_to_db(self, record: Record):
        sleep(randint(1, 3))
        logging.info("Wrote %s to DB", record)
