from src.app.Model.Abstract.DbConnection import DbConnection


class Creator(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self._id = None
        self.name = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, _id, name FROM creator WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()

        self.id = result[0]
        self._id = result[1]
        self.name = result[2]

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO creator (id, _id, name)" \
                " VALUES (%(id)s, %(_id)s, %(name)s);"
        cur.execute(query, {'id': data['id'], "_id": data['_id'], "name": data['name']})
        cur.execute('SELECT LASTVAL()')
        result = cur.fetchone()
        return result[0]
