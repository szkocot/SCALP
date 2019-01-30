from src.app.Model.User import User

import hashlib


class AuthService:
    user = None

    def __init__(self):
        self.user = User
        return

    def login(self, request):
        if self.isRegistered(request.form['username']):
            return self.validateUser(request)
        else:
            return 'Please register first'

    def isRegistered(self, request):
        if self.user.userExsists(request.form['username']):
            return True
        else:
            return False

    def validateUser(self, request):
        if hashlib.sha256(request.form['password']) == self.user.getUserPasswordHash(request.form['username']):
            return "Success"
        else:
            return 'Wrong Password'

    def createUser(self, request):
        if self.user.userExsists(request.form['username']):
            return "Username taken!"
        else:
            self.user.create(request.form['username'], hashlib.sha256(request.form['password']), request.form['name'],
                             request.form['surname'], request.form['email'])
            return "Success"
