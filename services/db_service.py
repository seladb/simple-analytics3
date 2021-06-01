import logging
from random import randint
from time import sleep
from common.record import Record


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class DBService:
    def write_to_db(self, record: Record):
        sleep(randint(1, 3))
        logger.info("Wrote %s to DB", record)
