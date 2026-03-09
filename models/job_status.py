from enum import Enum

class JobStatus(str, Enum):
    PENDING = 'PENDING'
    QUEUED = 'QUEUED'
    RUNNING = 'RUNNING'
    SUCCESSFULL = 'SUCCESSFULL'
    FAILED = 'FAILED'
    RETRY = 'RETRY'