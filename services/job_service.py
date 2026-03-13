from db.session import SessionLocal
from models.jobs import Job
from core.redis_client import redis_client
from core.queue import JOB_QUEUE


def create_job(payload, priority=0):
    db = SessionLocal()

    job = Job(
        payload=payload,
        priority=priority
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    # push job id to Redis queue
    redis_client.lpush(JOB_QUEUE, str(job.id))

    return job