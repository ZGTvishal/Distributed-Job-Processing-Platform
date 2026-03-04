# scripts/test_infra.py
import core
from core.logger import logger
from core.queue import queue_client

logger.info("infra_test_start")

queue_client.push("test-job-123")

print("Queue size:", queue_client.size())