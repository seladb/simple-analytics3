import logging
from random import randint
from time import sleep


class EnrichGeoLocation:
    def enrich(self, ip_address: str) -> str:
        sleep(randint(1, 3))
        enriched_data = f"Enriched data for {ip_address}"
        logging.info(enriched_data)
        return enriched_data
