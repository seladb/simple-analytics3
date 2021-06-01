from dataclasses import dataclass
from flask import Request


@dataclass()
class Record:
    geo_location: str
    rank: int
    request: Request
