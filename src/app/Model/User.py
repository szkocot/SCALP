from .DbConnection import DbConnection


class User(DbConnection):
    def userExsists(self, username):
        db = self.getCursor()
        query = "SELECT id FROM users WHERE username = %s"
        result = db.execute(query, username).fetchall()
        if result is not None and len(result) > 0:
            return True
        else:
            return False

    def getUserById(self, id):
        db = self.getCursor()
        query = "SELECT id, username, name, surname, email FROM users WHERE id = %d"
        result = db.execute(query, id)
        return result

    def getUserPasswordHash(self, username):
        db = self.getCursor()
        query = "SELECT password FROM users WHERE username = %s"
        result = db.execute(query, username).fetchone()
        return result['password']

    def create(self, username, password, name=None, surname=None, email=None):
        db = self.getCursor()
        query = "INSERT INTO user (username, password, name, surname, email) VALUES (%s, %s, %s, %s, %s);"
        return db.execute(query, (username, password, name, surname, email))
