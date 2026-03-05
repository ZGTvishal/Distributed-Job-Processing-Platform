import uuid
from sqlalchemy import String, DateTime, Integer, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    job_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id")
    )

    task_type: Mapped[str] = mapped_column(String(255))

    payload: Mapped[dict] = mapped_column(JSONB)

    status: Mapped[str] = mapped_column(
        Enum(
            "pending",
            "running",
            "success",
            "failed",
            name="task_status"
        ),
        default="pending"
    )

    retries: Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )