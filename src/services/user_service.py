from entities.user import User
from repositories.user_repository import user_repository


class UserExistsError(Exception):
    pass


class UserService:

    def __init__(self):
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


user_service = UserService()
