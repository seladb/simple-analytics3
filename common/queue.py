from typing import Optional


class Job:
    pass


class JobQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, job: Job):
        new_node = job
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def dequeue(self) -> Optional[Job]:
        job = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return job
