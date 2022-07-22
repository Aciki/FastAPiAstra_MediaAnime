from fastapi import FastAPI
import uvicorn
from cassandra.cqlengine.management import sync_table

from .users import models

from .config import get_settings
from .db import get_session

DB_SESSION = None


main_app = FastAPI()
settings = get_settings()


@main_app.on_event("startup")
def on_startup():
    global DB_SESSION
    DB_SESSION = get_session()
    sync_table(models.User)
    print("Starting")


@main_app.get("/")
def homepage():
    return {"heloo": "Friend"}


if __name__ == "__main__":
    uvicorn.run(main_app, host="localhost", port=8000)
