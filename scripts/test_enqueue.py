from services.job_service import create_job

job = create_job(
    payload={"task": "send_email", "user_id": 42},
    priority=1
)

print("Job created:", job.id)