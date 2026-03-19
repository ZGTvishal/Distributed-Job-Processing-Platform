from datetime import datetime

def get_job_by_id(db, job_id):
    from models.jobs import Job
    return db.query(Job).filter(Job.id == job_id).first()


def mark_started(db, job, worker_id):
    job.status = "STARTED"
    job.started_at = datetime.utcnow()
    job.worker_id = worker_id
    db.commit()


def mark_success(db, job):
    job.status = "SUCCESS"
    job.finished_at = datetime.utcnow()
    db.commit()


def mark_failed(db, job, error_msg):
    job.status = "FAILED"
    job.finished_at = datetime.utcnow()
    job.retry_count += 1
    db.commit()