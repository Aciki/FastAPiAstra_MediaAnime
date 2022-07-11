import os
from pathlib import Path
from functools import lru_cache
from pydantic import BaseSettings, Field
from dotenv import load_dotenv

load_dotenv()

os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = "1"


class Settings(BaseSettings):
    keyspace: str = Field(..., env="ASTRADB_KEYSPACE")
    db_client_id: str = Field(..., env="db_client_id")
    db_client_secret: str = Field(..., env="db_client_secret")

    class Config:
        case_sensitive = False
        env_file = ".env"  # This is the key factor


@lru_cache
def get_settings():
    return Settings()
