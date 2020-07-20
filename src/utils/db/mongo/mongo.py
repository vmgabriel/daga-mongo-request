# Develop: vmgabriel

"""Definion of Module Class for Mongo Connection"""

# Libraries
import pymongo

# Absracts
from src.domain.models.db_connection import Db_Connection

# Configuration
from src.config.server import configuration as conf


class Mongo_Connection(Db_Connection):
    """Monngo Class for Connection"""
    def __init__(self):
        self.conn = None
        self.cursor = None

        try:
            if not self.conn:
                self.conn = pymongo.MongoClient(self.connector())
            self.conn.server_info()
            print('[DATABASE] - Database Connected')
        except pymongo.errors.ServerSelectionTimeoutError as err:
            # do whatever you need
            print(err)

    def get_connection(self):
        """Return Connection"""
        return self.conn

    def get_cursor(self):
        """Return the Cursor"""
        return self.conn[conf['db_name_database']]

    def migrations(self) -> None:
        """Migrate data"""

    def disconnect(self):
        """Disconnect of database"""
        try:
            self.conn.close()
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print(err)
        finally:
            print('DATABASE: Connection closed.')

    def connector(self, is_inicialized: bool = True)  -> str:
        """Return Connector Uri"""
        return 'mongodb://{}:{}@{}:{}'.format(
            conf['user_database'],
            conf['password_database'],
            conf['host_database'],
            conf['port_database']
        )
