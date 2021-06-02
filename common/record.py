from dataclasses import dataclass


@dataclass()
class Record:
    geo_location: str
    rank: int
