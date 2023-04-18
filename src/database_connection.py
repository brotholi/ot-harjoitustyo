import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "databases", "database.sqlite"))
connection.row_factory = sqlite3.Row


def create_database_connection():
    return connection
