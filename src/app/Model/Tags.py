from src.app.Model.Abstract.DbConnection import DbConnection


class Tags(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.data = None
        self.note_id = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, data, note_id FROM tags WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.data = result[1]
        self.note_id = result[2]

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO tags(id, data, note_id)" \
                " VALUES (%(id)s, %(data)s, %(note_id)s);"
        cur.execute(query, {'id': data['id'], "data": data['data'], "note_id": data['note_id']})
        return
