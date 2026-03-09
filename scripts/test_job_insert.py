from db.session import SessionLocal
from models.job import Job

db = SessionLocal()

job = Job(
    payload={"task": "send_email", "user_id": 123},
    priority=1
)

db.add(job)
db.commit()

print("Created job:", job.id)