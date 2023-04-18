from entities.user import User
from database_connection import create_database_connection


class UserRep:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from lihasloki_users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from lihasloki_users")
        self._connection.commit()

# syöttää käyttäjän tiedot tauluun
    def create_new_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("insert into lihasloki_users (username, password) values (?, ?)",
                       (user.username, user.password)
                       )
        self._connection.commit()
        return user

# hakee yhden käyttäjän tiedot
    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select * from lihasloki_users where username = ?",
                       (username,))

        row = cursor.fetchone()
        return User(row["username"], row["password"]) if row else None


user_repository = UserRep(create_database_connection())
lihasloki_users = user_repository.find_all()
