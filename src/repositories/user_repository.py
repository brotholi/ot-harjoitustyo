import sqlite3
import sys
from entities.user import User
from database_connection import create_database_connection


class DatabaseDoesNotExistError(Exception):
    pass


class UserRep:
    """Luokka, joka vastaa sovelluksen käyttäjiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyteen liittyvä Connection-olio
        """
        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki tietokannassa olevat käyttäjät.
        Returns:
            Palauttaa listan User-olioita.
        """
        cursor = self._connection.cursor()
        try:
            cursor.execute("select * from lihasloki_users")
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

    def delete_all(self):
        """Poistaa kaikki käyttäjät.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from lihasloki_users")
        self._connection.commit()

    def create_new_user(self, user):
        """Syöttää käyttäjän tiedot tauluun.
        Args:
            user: Tallennettava käyttäjä User-oliona.
        Returns:
            Tallennettu käyttäjä User-oliona.
        """

        cursor = self._connection.cursor()
        try:
            cursor.execute("insert into lihasloki_users (username, password) values (?, ?)",
                           (user.username, user.password)
                           )
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        self._connection.commit()
        return user

    def find_by_username(self, username):
        """Hakee yhden käyttäjän tiedot käyttäjätunnuksen perusteella.
        Args:
            username: Käyttäjätunnus, jonka omaava käyttäjä palautetaan.
        Returns:
            Palauttaa User-olion, jos käyttäjätunnuksen käyttäjä on tietokannassa.
            Muutoin palauttaa None.
        """

        cursor = self._connection.cursor()
        try:
            cursor.execute("select * from lihasloki_users where username = ?",
                           (username,))
        except sqlite3.OperationalError:
            self._handle_nonexistent_database_error()
        row = cursor.fetchone()
        return User(row["username"], row["password"]) if row else None

    def _handle_nonexistent_database_error(self):
        """Jos tietokantaa ei ole alustettu, lopettaa sovelluksen.
        """
        print("Tietokantaa ei ole olemassa,tee ensin alustukset komennolla poetry run invoke build")
        sys.exit()


user_repository = UserRep(create_database_connection())
