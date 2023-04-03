import unittest
from services.user_service import UserService
from entities.user import User

class TestCreateUser(unittest.TestCase):
    def setUp(self):
        pass

    def test_createuser(self):
        service = UserService()
        username = "Mollamaija"
        password = "Sal4san4"
        user = service.create_new_user(username, password)
        self.assertEqual(user.username, "Mollamaija")