import uuid
from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID

from db.base import Base
from models.job_status import JobStatus


class Job(Base):
    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    status = Column(
        Enum(JobStatus),
        nullable=False,
        default=JobStatus.PENDING
    )

    payload = Column(JSON, nullable=False)

    priority = Column(Integer, default=0)

    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)

    worker_id = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime, nullable=True)
    finished_at = Column(DateTime, nullable=True)