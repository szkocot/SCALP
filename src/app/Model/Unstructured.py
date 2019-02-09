from src.app.Model.Abstract.DbConnection import DbConnection


class Unstructured(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.diagnosis = None
        self.id1 = None
        self.localization = None
        self.site = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, diagnosis, id1, localization, site FROM public.unstructured WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.diagnosis = result[1]
        self.id1 = result[2]
        self.localization = result[3]
        self.site = result[4]
        return self

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO public.unstructured(diagnosis, id1, localization, site)" \
                " VALUES (%(diagnosis)s, %(id1)s, %(localization)s, %(site)s);"
        cur.execute(query, {"diagnosis": data.get('diagnosis'), "id1": data.get('id1'),
                            'localization': data.get('localization'), "site": data.get('site')})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
