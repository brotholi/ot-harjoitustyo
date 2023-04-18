import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRep(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self._user_maija = User("maija", "jaatelo22")
        self._user_unto = User("unto", "musiik1a")

    def test_create_new_user(self):
        user_repository.create_new_user(self._user_maija)
        user = user_repository.find_by_username(self._user_maija.username)
        self.assertEqual(user.username, self._user_maija.username)
        lihasloki_users = user_repository.find_all()
        self.assertEqual(len(lihasloki_users), 1)

    def test_find_all_users(self):
        user_repository.create_new_user(self._user_maija)
        user_repository.create_new_user(self._user_unto)
        lihasloki_users = user_repository.find_all()
        self.assertEqual(len(lihasloki_users), 2)
