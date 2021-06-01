from random import randint
from time import sleep
from flask import Request


class AnomalyRanking:
    def rank_request(self, request: Request) -> int:
        sleep(randint(1, 3))
        return randint(1, 1000)
