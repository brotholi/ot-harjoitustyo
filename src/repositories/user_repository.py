import sqlite3
import sys
from entities.user import User
from database_connection import create_database_connection


class DatabaseDoesNotExistError(Exception):
    pass


class UserRep:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        try:
            cursor.execute("select * from lihasloki_users")
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from lihasloki_users")
        self._connection.commit()

# syöttää käyttäjän tiedot tauluun
    def create_new_user(self, user):
        cursor = self._connection.cursor()
        try:
            cursor.execute("insert into lihasloki_users (username, password) values (?, ?)",
                           (user.username, user.password)
                           )
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        self._connection.commit()
        return user

# hakee yhden käyttäjän tiedot
    def find_by_username(self, username):
        cursor = self._connection.cursor()
        try:
            cursor.execute("select * from lihasloki_users where username = ?",
                           (username,))
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        row = cursor.fetchone()
        return User(row["username"], row["password"]) if row else None

    def _handle_nonexistent_database_error(self):
        print("Tietokantaa ei ole olemassa,tee ensin alustukset komennolla poetry run invoke build")
        sys.exit()


user_repository = UserRep(create_database_connection())
