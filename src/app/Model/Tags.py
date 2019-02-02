from src.app.Model.Abstract.DbConnection import DbConnection


class Tags(DbConnection):

    def __init__(self):
        super().__init__()
        self.tags = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, data, notes_id FROM tags WHERE notes_id = %(id)s"
        cur.execute(query, {'id': id})
        self.tags = cur.fetchAll()

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO tags(id, data, notes_id)" \
                " VALUES (%(id)s, %(data)s, %(notes_id)s);"
        cur.execute(query, {'id': data['id'], "data": data['data'], "notes_id": data['notes_id']})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
