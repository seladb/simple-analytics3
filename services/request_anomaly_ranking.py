import logging
from random import randint
from time import sleep


class AnomalyRanking:
    def rank_request(self, request_headers: dict) -> int:
        sleep(randint(1, 3))
        request_rank = randint(1, 1000)
        logging.info(f"Request rank: {request_rank}")
        return request_rank
