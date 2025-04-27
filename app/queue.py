import redis
import json
from typing import Any

class Queue:
    def enqueue(self, data: dict) -> None:
        raise NotImplementedError

    def dequeue(self) -> dict | None:
        raise NotImplementedError


class RedisQueue(Queue):
    # # use 'localhost' instead of 'redis' as host if running locally
    def __init__(self, host="redis", port=6379, queue_name="item_queue"):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)
        self.queue_name = queue_name

    def enqueue(self, data: dict) -> None:
        self.client.lpush(self.queue_name, json.dumps(data))

    def dequeue(self) -> dict | None:
        job = self.client.brpop(self.queue_name, timeout=5)
        if job:
            _, raw_data = job
            return json.loads(raw_data)
        return None
