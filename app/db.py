import pathlib
from cassandra.cluster import Cluster

from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection

from .config import get_settings

BASE_DIR = pathlib.Path(__file__).resolve().parent

ASTRADB_CONNECTION_FILE = BASE_DIR / "hiden" / "astraDB.zip"

settings = get_settings()
print(settings.db_client_id)
CLIENT_ID = settings.db_client_id
CLIENT_SECRET = settings.db_client_secret


def get_session():
    cloud_config = {"secure_connect_bundle": ASTRADB_CONNECTION_FILE}
    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    return session
