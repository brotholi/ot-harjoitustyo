from entities.user import User
from repositories.user_repository import UserRep

class UserService:

    def __init__(self, user_repository):
        self._user = None
        self._user_repository = user_repository
        
#luo uuden käyttäjän

    def create_new_user(self, username, password, password_check):
        if password == password_check:
            new_user = User(username, password)
            self._user_repository.create_new_user(new_user)
        
        else:
            print("passwords do not match")

user_service = UserService()
        

    