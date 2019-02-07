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
        query = 'SELECT id, accepted, "userId" FROM reviewed WHERE id = %(id)s'
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.accepted = result[1]
        self.time = result[2]
        self.userId = result[3]
        return self

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = 'INSERT INTO reviewed (accepted, "userId", "time") VALUES (%(accepted)s, %(userId)s, %(time)s);'
        cur.execute(query, {"accepted": data.get('accepted'), 'userId': data.get('userId'), 'time': data.get('time')})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
