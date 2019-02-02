from src.app.Model.Abstract.DbConnection import DbConnection


class User(DbConnection):

    def __init__(self):
        super().__init__()

    def userExsists(self, username):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id FROM users WHERE username = %(username)s"
        cur.execute(query, {'username': username})
        result = cur.fetchall()
        if result is not None and len(result) > 0:
            return True
        else:
            return False

    def getUserById(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, username, name, surname, email FROM users WHERE id = %(id)s"
        result = cur.execute(query, {'id': id})
        return result

    def getUserPasswordHash(self, username):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT password FROM users WHERE username = %(username)s"
        cur.execute(query, {'username': username})
        result = cur.fetchone()
        return result[0]

    def create(self, username, password, name=None, surname=None, email=None):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO users (username, password, name, surname, email) VALUES (%(username)s, %(password)s, %(name)s, %(surname)s, %(email)s);"
        cur.execute(query,
                    {'username': username, "password": password, "name": name, "surname": surname, "email": email})
        return
