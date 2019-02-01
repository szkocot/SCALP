from src.app.Model.User import User

import hashlib


class AuthService:
    user = None

    def __init__(self):
        self.user = User()
        return

    def login(self, data):
        if self.isRegistered(data['username']):
            return self.validateUser(data)
        else:
            return 'Please register first'

    def isRegistered(self, data):
        if self.user.userExsists(username=data['username']):
            return True
        else:
            return False

    def validateUser(self, data):
        if hashlib.sha256(data['password']) == self.user.getUserPasswordHash(username=data['username']):
            return "Success"
        else:
            return 'Wrong Password'

    def createUser(self, data):
        if self.user.userExsists(username=data['username']):
            return "Username taken!"
        else:
            self.user.create(data['username'], hashlib.sha256(data['password']), data['name'],
                             data['surname'], data['email'])
            return "Success"
