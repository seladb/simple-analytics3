from common.queue import JobQueue, Job


class TestJobQueue:
    def test_queue(self):
        jq = JobQueue()
        jq.enqueue(Job(id=1))
        jq.enqueue(Job(id=2))
        jq.enqueue(Job(id=3))
        assert jq.dequeue().id == 1
        assert jq.dequeue().id == 2
        assert jq.dequeue().id == 3
        assert jq.dequeue() is None
        jq.enqueue(Job(id=4))
        assert jq.dequeue().id == 4
        assert jq.dequeue() is None
