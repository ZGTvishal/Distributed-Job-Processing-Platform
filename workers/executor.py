import time

def execute_job(job):
    payload = job.payload

    print(f"Executing job {job.id} with payload {payload}")

    time.sleep(2)  # simulate work