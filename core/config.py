from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = Field(alias="APP_NAME")
    env: str = Field(alias="ENV")

    database_url: str = Field(alias="DATABASE_URL")

    redis_host: str = Field(alias="REDIS_HOST")
    redis_port: int = Field(alias="REDIS_PORT")
    redis_db: int = Field(alias="REDIS_DB")

    worker_timeout_seconds: int = Field(alias="WORKER_TIMEOUT_SECONDS")
    max_retries: int = Field(alias="MAX_RETRIES")

    log_level: str = Field(alias="LOG_LEVEL")


def get_settings():
    return Settings()


settings = get_settings()