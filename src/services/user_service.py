from entities.user import User
# from ..repositories.user_repository import UserRep


class UserService:

    def __init__(self):
        self._user = None

    def create_new_user(self, username, password):
        # luodaan uusi user-olio
        new_user = User(username, password)
        # viedään uuden käyttäjän tiedot tietokantaan
        # user = self._user_repository.create_new_user(new_user)
        return new_user
