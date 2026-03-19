# Distributed Job Processing Platform

A production-oriented distributed job processing system built with Python, designed to simulate real-world background task execution similar to systems like Celery and Sidekiq.

---

## 🚀 Overview

This project implements a scalable architecture for processing asynchronous jobs using:

* Persistent job storage
* Distributed queueing
* Worker-based execution model

It demonstrates backend engineering concepts such as:

* system design
* asynchronous processing
* queue-based architecture
* fault tolerance (planned)
* horizontal scalability (planned)

---

## 🧠 Architecture

```
Client / Producer
        │
        ▼
PostgreSQL (Job Metadata)
        │
        ▼
Redis Queue (Job IDs)
        │
        ▼
Worker Processes (Execution Engine)
```

### Components

* **Producer** → creates jobs
* **Database** → stores job state and metadata
* **Queue** → distributes work
* **Worker** → executes tasks

---

## 🛠️ Tech Stack

* Backend: Python
* ORM: SQLAlchemy
* Migrations: Alembic
* Queue: Redis
* Database: PostgreSQL
* Containerization: Docker

---

## 📂 Project Structure

```
project-root/
│
├── core/              # Config, logging, queue client
├── db/                # Database session & base
├── models/            # ORM models
├── services/          # Business logic
├── scripts/           # Test scripts
├── migrations/        # Alembic migrations
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <repo-url>
cd project-root
```

---

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Start infrastructure (Docker)

#### PostgreSQL

```
docker run -d \
  --name local-postgres \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=jobs_db \
  postgres
```

#### Redis

```
docker run -d \
  --name local-redis \
  -p 6379:6379 \
  redis
```

---

### 5. Configure environment variables

Create a `.env` file:

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/jobs_db
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
LOG_LEVEL=INFO
```

---

### 6. Run migrations

```
alembic upgrade head
```

---

## 🧪 Testing the System

### Create and enqueue a job

```
python -m scripts.test_enqueue
```

Expected output:

```
Job created: <uuid>
```

---

### Verify queue in Redis

```
docker exec -it local-redis redis-cli
```

```
LRANGE job_queue 0 -1
```

---

## 🧩 Job Model

| Field       | Description              |
| ----------- | ------------------------ |
| id          | Unique job identifier    |
| status      | PENDING / RUNNING / DONE |
| payload     | JSON task data           |
| priority    | Job priority             |
| retry_count | Retry attempts           |
| max_retries | Max retry limit          |
| created_at  | Job creation time        |
| started_at  | Execution start time     |
| finished_at | Completion time          |
| worker_id   | Assigned worker          |

---

## 🔄 Current Workflow

1. Job is created via service
2. Stored in PostgreSQL
3. Job ID pushed to Redis queue
4. Worker (next phase) will process it

---

## 🧱 Upcoming Features

* Worker execution engine
* Retry mechanism with backoff
* Dead letter queue
* Priority queue support
* Rate limiting
* Job scheduling (cron-like)
* Monitoring dashboard

---

## 📈 Why This Project Matters

This project demonstrates:

* Real-world backend system design
* Distributed systems fundamentals
* Queue-based processing
* Production-ready architecture thinking

It is intentionally designed to reflect patterns used in systems like:

* Celery
* Sidekiq
* AWS SQS + Workers

---

## 🧑‍💻 Author

Vishal Patel
MSc Computer Science, University of Liverpool
Software Engineer (Backend & Full-stack)

---

## 📄 License

MIT License
