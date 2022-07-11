from fastapi import FastAPI
import uvicorn
from cassandra.cqlengine.management import sync_table
from .users.models import User

from . import config, db

DB_SESSION = None


main_app = FastAPI()
settings = config.get_settings()


@main_app.on_event("startup")
def on_startup():
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)
    print("Starting")


@main_app.get("/")
def homepage():
    return {"heloo": "Friend"}


if __name__ == "__main__":
    uvicorn.run(main_app, host="localhost", port=8000)
