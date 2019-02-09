from src.app.Model.Abstract.DbConnection import DbConnection


class User(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.username = None
        self.password = None
        self.name = None
        self.surname = None
        self.email = None
        self.admin = None
        self.checked_images = None

    def getUserData(self, username):
        if self.username is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, username, password, name, surname, email, admin, checked_images FROM users WHERE username = %(username)s"
            cur.execute(query, {'username': username})
            result = cur.fetchone()
            self.id = result[0]
            self.username = result[1]
            self.password = result[2]
            self.name = result[3]
            self.surname = result[4]
            self.email = result[5]
            self.admin = result[6]
            self.checked_images = result[7]
            return self
        else:
            return self

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
        if self.id is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, username, password, name, surname, email, admin, checked_images FROM users WHERE id = %(id)s"
            cur.execute(query, {'id': id})
            result = cur.fetchone()
            self.id = id
            self.username = result[1]
            self.password = result[2]
            self.name = result[3]
            self.surname = result[4]
            self.email = result[5]
            self.admin = result[6]
            self.checked_images = result[7]
            return self
        else:
            return self

    def getUserPasswordHash(self, username):
        if self.password is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT password FROM users WHERE username = %(username)s"
            cur.execute(query, {'username': username})
            result = cur.fetchone()
            return result[0]
        else:
            return self.password

    def create(self):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO users (username, password, name, surname, email) VALUES (%(username)s, %(password)s, %(name)s, %(surname)s, %(email)s);"
        cur.execute(query,
                    {'username': self.username, "password": self.password, "name": self.name, "surname": self.surname,
                     "email": self.email})
        cur.execute('SELECT LASTVAL()')
        result = cur.fetchone()
        return result[0]

    def checkAdmin(self, username):
        if self.admin is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT admin FROM users WHERE username = %(username)s"
            cur.execute(query, {'username': username})
            result = cur.fetchone()
            return result[0]
        else:
            return self.admin

    def update(self):
        if self.admin == 'on':
            admin = True
        else:
            admin = False
        db = self.getConnection()
        cur = db.cursor()
        query = "UPDATE users SET name = %(name)s, surname = %(surname)s, password = %(password)s, email = %(email)s , admin = %(admin)s WHERE id = %(id)s "
        return cur.execute(query,
                           {'name': self.name, 'surname': self.surname, 'email': self.email, 'id': self.id,
                            'admin': admin, 'password': self.password})

    def deleteUser(self):
        db = self.getConnection()
        cur = db.cursor()
        query = "DELETE FROM users WHERE id = %(id)s"
        return cur.execute(query, {'id': self.id})

    def updateCheckedImages(self):
        db = self.getConnection()
        cur = db.cursor()
        query = """UPDATE users 
                  SET checked_images =  
                  ((SELECT checked_images FROM users where id = %(id)s) + 1)
                  WHERE id = %(id)s """
        return cur.execute(query, {'id': self.id})
