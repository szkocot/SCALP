from src.app.Model.Abstract.DbConnection import DbConnection


class Unstructured(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.data = None
        self.note_id = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, diagnosis, id1, localization, site FROM unstructured WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.data = result[1]
        self.note_id = result[2]

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO unstructured(diagnosis, id1, localization, site)" \
                " VALUES (%(diagnosis)s, %(id1)s, %(localization)s, %(site)s);"
        cur.execute(query, {"diagnosis": data['diagnosis'], "id1": data['id1'],
                            'localization': data['localization'], "site": data['site']})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
