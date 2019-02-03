from src.app.Model.Abstract.DbConnection import DbConnection


class Notes(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.reviewed = None
        self.tag = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = 'SELECT id, "reviewedId" FROM notes WHERE id = %(id)s'
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.reviewed = result[1]

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = 'INSERT INTO notes(reviewed_id, tags) VALUES (%(reviewed_id)s, %(tags)s);'
        cur.execute(query, {'reviewed_id': data.get('reviewedId'), 'tags': data.get('tags')})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
