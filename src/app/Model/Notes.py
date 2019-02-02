from src.app.Model.Abstract.DbConnection import DbConnection


class Notes(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.reviewed = None
        self.tags = None

    # todo to jest zjebane do przepisania
    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, reviewed FROM notes WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.reviewed = result[1]

    def insert(self, reviewedId):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO notes(reviewedId) VALUES (%(reviewedId)s);"
        cur.execute(query, {'reviewedId': reviewedId})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
