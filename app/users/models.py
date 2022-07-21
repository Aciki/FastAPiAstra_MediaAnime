from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid
import sys

sys.path.append("..")
import config

settings = config.get_settings()


class User(Model):
    __keyspace__ = settings.keyspace
    user_id = columns.Text(primary_key=True, default=uuid.uuid1)
    email = columns.Text(primary_key=True)
    password = columns.Text()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"User(email = {self.email},user_id = {self.user_id}"
