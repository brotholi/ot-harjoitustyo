import unittest
from repositories.user_repository import user_repository
from services.user_service import UserService, UserExistsError, InvalidCredentialsError
from entities.user import User


class FakeTestUserRep:
    def __init__(self, lihasloki_users=None, user=None):
        self._user = user
        self.users = lihasloki_users or []

    def create_new_user(self, user):
        self.users.append(user)

        return user

    def find_by_username(self, username):
        matching_users = filter(
            lambda user: user.username == username,
            self.users
        )
        list_matching = list(matching_users)

        if len(list_matching) > 0:
            return list_matching[0]

        return None


class TestUserService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_service = UserService(FakeTestUserRep())
        self.user_maija = User("Mollamaija", "Sal4san4")

    def login_user(self, user):
        self.user_service.create_new_user(user.username, user.password)

    def test_create_valid_user(self):
        username = self.user_maija.username
        password = self.user_maija.password
        self.user_service.create_new_user(username, password)
        self.assertEqual(username, "Mollamaija")

    def test_create_existing_user(self):
        username = "Mollamaija"
        password = "heppa"
        self.user_service.create_new_user(username, password)
        self.assertRaises(
            UserExistsError,
            lambda: self.user_service.create_new_user(username, 'random')
        )

    def test_login(self):
        username = self.user_maija.username
        password = self.user_maija.password
        self.user_service.create_new_user(username, password)
        user = self.user_service.login(username, password)
        self.assertEqual(user.username, self.user_maija.username)

        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.user_service.login(username, 'haukionkala')
        )
