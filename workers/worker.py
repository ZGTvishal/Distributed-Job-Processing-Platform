import uuid
from core.queue import queue_client
from db.session import SessionLocal
from workers.executor import execute_job
from workers.state_manager import (
    mark_started,
    mark_success,
    mark_failed,
    get_job_by_id
)

WORKER_ID = str(uuid.uuid4())

def start_worker():
    print(f"Worker started: {WORKER_ID}")

    while True:
        job_id = queue_client.blocking_pop()

        job_id = job_id.decode()

        db = SessionLocal()

        try:
            job = get_job_by_id(db, job_id)

            if not job:
                continue

            mark_started(db, job, WORKER_ID)

            execute_job(job)

            mark_success(db, job)

        except Exception as e:
            mark_failed(db, job, str(e))

        finally:
            db.close()