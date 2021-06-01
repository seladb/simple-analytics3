from random import randint
from time import sleep


class EnrichGeoLocation:
    def enrich(self, ip_address: str) -> str:
        sleep(randint(1, 3))
        return f"Enriched data for {ip_address}"
