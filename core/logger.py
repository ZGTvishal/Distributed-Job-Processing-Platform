# core/logger.py

import logging
import structlog
from core.config import settings


def configure_logging():
    logging.basicConfig(
        format="%(message)s",
        level=settings.LOG_LEVEL,
    )

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


configure_logging()

logger = structlog.get_logger()