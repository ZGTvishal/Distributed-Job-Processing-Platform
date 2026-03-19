# core/queue.py

import redis
from core.config import settings
from core.logger import logger


class QueueClient:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            decode_responses=True
        )
        self.queue_name = "job_queue"

    def enqueue(self, job_id: str):
        self.client.lpush(self.queue_name, job_id)
        logger.info("job_enqueued", job_id=job_id)

    def dequeue_blocking(self, timeout=0):
        result = self.client.brpop(self.queue_name, timeout=timeout)
        if result:
            _, job_id = result
            logger.info("job_dequeued", job_id=job_id)
            return job_id
        return None

    def size(self):
        return self.client.llen(self.queue_name)


queue_client = QueueClient()


queue_client = QueueClient()