from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class UserService:
    """Käyttäjiin liittyvästä sovelluslogiikasta vastaava luokka."""

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori. Luo uuden käyttäjien sovelluslogiikasta vastaavan palvelun.
        Args:
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepositoryn olio.
                Oliolla on UserRepository-luokkaa vastaavat metodit.
        """

        self._user = None
        self._user_repository = user_repository

    def create_new_user(self, username, password):
        """Luo uuden käyttäjän.
        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa käyttäjän salasanaa.
        Returns:
            Luotu käyttäjä User-oliona.
        Raises:
            UserExistsError:
                Virhe, kun käyttäjätunnus on jo olemassa toisella käyttäjällä.
        """
        check_user_exists = self.check_if_user_exists(username)

        if check_user_exists:
            raise UserExistsError()
        new_user = User(username, password)
        self._user_repository.create_new_user(new_user)
        return new_user

    def check_if_user_exists(self, username):
        """Tutkii, onko käyttäjää olemassa.
        Args:
            username: Merkkijonoarvo, joka kuvastaa uuden käyttäjän käyttäjätunnusta.
        Returns:
            False, jos samannimistä käyttää ei vielä ole.
            True, jos käyttäjä on jo käytössä.
        """
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            return True

        return False

    def login(self, username, password):
        """Kirjaa nykyisen käyttäjän sisään.
        Args:
            username: Merkkijonoarvo, joka kuvaa kirjautumassa olevan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa kirjautumassa olevan käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä User-oliona.
        Raises:
            InvalidCredentialsError:
                Virhe, kun käyttäjätunnus ja salasana eivät täsmää.
        """

        current_user = self._user_repository.find_by_username(username)

        if not current_user or current_user.password != password:
            raise InvalidCredentialsError()
        self._user = current_user
        return current_user

    def get_current_user(self):
        """Paluttaa tällä hetkellä kirjautuunen käyttäjän.
        Returns:
            Kirjautunut käyttäjä User-oliona.
        """
        username = self._user.username
        return username


user_service = UserService()
