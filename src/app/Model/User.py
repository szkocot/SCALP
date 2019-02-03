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
        query = "SELECT id, username, name, surname, email, admin FROM users WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
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
        cur.execute('SELECT LASTVAL()')
        result = cur.fetchone()
        return result[0]

    def checkAdmin(self, username):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT admin FROM users WHERE username = %(username)s"
        cur.execute(query, {'username': username})
        result = cur.fetchone()
        return result[0]

    def update(self, data):
        if data.get('admin') == 'on':
            admin = True
        else:
            admin = False
        db = self.getConnection()
        cur = db.cursor()
        query = "UPDATE users SET name = %(name)s, surname = %(surname)s, email = %(email)s , admin = %(admin)s WHERE id = %(id)s "
        return cur.execute(query, {'name': data['name'], 'surname': data['surname'], 'email': data['email'], 'id':data['id'], 'admin': admin})

    def deleteUser(self,id):
        db = self.getConnection()
        cur = db.cursor()
        query = "DELETE FROM users WHERE id = %(id)s"
        return cur.execute(query, {'id': id})
