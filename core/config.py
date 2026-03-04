# core/config.py

from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    APP_NAME: str = "Distributed Job Processing Platform"
    ENV: str = Field(default="development")

    # Database
    DATABASE_URL: str = Field(...)

    # Redis
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    # Worker
    WORKER_TIMEOUT_SECONDS: int = 60
    MAX_RETRIES: int = 3

    # Logging
    LOG_LEVEL: str = "INFO"

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
    }


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()