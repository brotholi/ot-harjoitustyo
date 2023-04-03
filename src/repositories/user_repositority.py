from database_connection import database_connection
from entities.user import User

class UserRep:
    def __init__(self, connection):
        self._connection = connection

#syöttää käyttäjän tiedot tauluun

    def create_new_user(self, user):

        cursor = self._connection.cursor()
        
        cursor.execute("insert into lihasloki_users (username, password) values (?, ?)",
            (user.username, user.password)
        )


user_repository = UserRep(database_connection())
