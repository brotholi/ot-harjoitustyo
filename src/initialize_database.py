# import sqlite3
from database_connection import create_database_connection


def initialize_database():
    connection = create_database_connection
    drop_tables(connection)
    create_tables(connection)


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        drop table if exists lihasloki_users; """)
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(("""
        create table lihasloki_users (
            username text primary key,
            password text
        );
        """))
    connection.commit()


if __name__ == "__main__":
    initialize_database()
