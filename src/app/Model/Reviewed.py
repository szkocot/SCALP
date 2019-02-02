from src.app.Model.Abstract.DbConnection import DbConnection


class Reviewed(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.accepted = None
        self.time = None
        self.userId = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, accepted, userId FROM notes WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.accepted = result[1]
        self.time = result[2]
        self.userId = result[3]

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO notes(id, accepted, userId)" \
                " VALUES (%(id)s, %(accepted)s, %(userId)s);"
        cur.execute(query, {'id': data['id'], "accepted": data['accepted'], 'userId': data['userId']})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
