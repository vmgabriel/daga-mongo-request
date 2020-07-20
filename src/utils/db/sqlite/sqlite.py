# Develop: vmgabriel

"""Module for Sqlite Connect"""

# Libraries
import sqlite3

# Absracts
from src.domain.models.db_connection import Db_Connection
from src.config.server import configuration as conf

# Call definition
from src.counter_five.infraestructures.sqlite.entities.definitions import get_definition


class SQLiteConnection(Db_Connection):
    """Sqlite Class Connection """
    def __init__(self):
        self.conn = None
        self.cursor = None

        try:
            self.conn = sqlite3.connect(
                self.connector(),
                check_same_thread=False
            )
            print('[DATABASE SQLITE] - Database Connected')
            print('[DATABASE SQLITE] - Genering migration')
            self.migrations()
        except sqlite3.OperationalError as error:
            print('Error:', error)

    def get_connection(self):
        """Return the Connection"""
        return self.conn

    def get_cursor(self):
        """Return cursor or pool of connection"""
        return self.conn.cursor()

    def migrations(self) -> None:
        """Migrate data to database"""
        cursor = self.get_cursor()
        cursor.execute(get_definition())

    def disconnect(self):
        """Disconnect of Database"""
        try:
            self.conn.close()
        except Exception as err:
            print(err)
        finally:
            print('DATABASE SQLITE: Connection closed.')

    def connector(self, is_inicialized: bool = True)  -> str:
        """Return Connector Uri"""
        return '{}{}'.format(
            conf['path_migration'],
            conf['file_database']
        )
