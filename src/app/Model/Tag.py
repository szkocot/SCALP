from src.app.Model.Abstract.DbConnection import DbConnection


class Tag(DbConnection):

    def __init__(self):
        super().__init__()
        self.data = None
        self.id = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, data, FROM public.tag WHERE notes_id = %(id)s"
        cur.execute(query, {'id': id})
        self.tag = cur.fetchAll()
        return self

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = 'INSERT INTO public.tag("data") VALUES (%(data)s);'
        cur.execute(query, {"data": data})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
