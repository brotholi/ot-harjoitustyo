from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class UserService:

    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def create_new_user(self, username, password):
        # tarkastetaan, ettei käyttäjää ole olemassa
        check_user_exists = self.check_if_user_exists(username)

        if check_user_exists:
            raise UserExistsError()
        # luodaan olio new user
        # viedään uuden käyttäjän tiedot tietokantaan
        new_user = User(username, password)
        self._user_repository.create_new_user(new_user)
        return new_user

    def check_if_user_exists(self, username):
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            return True

        return False

    def login(self, username, password):
        current_user = self._user_repository.find_by_username(username)

        # tarkistetaan, että käyttäjä on olemassa ja salasana täsmää
        if not current_user or current_user.password != password:
            raise InvalidCredentialsError()
        # palautetaan käyttäjä
        self._user = current_user
        return current_user

    def get_current_user(self):
        username = self._user.username
        return username


user_service = UserService()
