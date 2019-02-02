from src.app.Model.Abstract.DbConnection import DbConnection


class Notes(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.accepted = None
        self.time = None
        self.user_id = None


    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, accepted, time, user_id FROM notes WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.accepted = result[1]
        self.time = result[2]
        self.user_id = result[3]


    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO notes(id, accepted, time, user_id)" \
                " VALUES (%(id)s, %(accepted)s, %(time)s, %(user_id)s);"
        cur.execute(query,
                    {'id': data['id'], "accepted": data['accepted'], "time": data['time'],
                     'user_id': data['user_id']})
        return
