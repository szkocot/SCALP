from src.app.Model.Abstract.DbConnection import DbConnection


class Meta(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.acquisition_id = None
        self.clinical_id = None
        self.unstructured_id = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, _acquisition_id, _clinical_id, unstructured_id FROM public.meta WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self.acquisition_id = result[1]
        self.clinical_id = result[2]
        self.unstructured_id = result[3]
        return self

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO public.meta (acquisition_id, clinical_id, unstructured_id)" \
                " VALUES (%(acquisition_id)s, %(clinical_id)s, %(unstructured_id)s);"
        cur.execute(query,
                    {"acquisition_id": data.get('acquisitionId'), "clinical_id": data.get('clinicalId'),
                     'unstructured_id': data.get('unstructuredId')})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
