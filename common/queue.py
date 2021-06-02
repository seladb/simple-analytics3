from typing import Optional


class Job:
    pass


class JobQueue:
    def __init__(self):
        pass

    def enqueue(self, job: Job):
        pass

    def dequeue(self) -> Optional[Job]:
        return None
