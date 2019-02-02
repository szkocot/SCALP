from src.app.Model.Abstract.DbConnection import DbConnection


class Metadata(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self._model_type = None
        self.created = None
        self.dataset_id = None
        self.name = None
        self.notes_id = None
        self.updated = None
        self._id = None
        self.creator_id = None
        self.meta_id = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, _acquisition_id, _clinical_id, unstructured_id FROM metadata WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self._model_type = result[1]
        self.created = result[2]
        self.dataset_id = result[3]
        self.name = result[4]
        self.notes_id = result[5]
        self.updated = result[6]
        self._id = result[7]
        self.creator_id = result[8]
        self.meta_id = result[9]

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO metadata(_model_type, created, dataset_id, name, notes_id, updated, _id, creator_id, meta_id)" \
                " VALUES (%(_model_type)s, %(created)s, %(dataset_id)s, %(name)s, %(notes_id)s, %(updated)s, %(_id)s, %(creator_id)s, %(meta_id)s);"
        cur.execute(query,
                    {'id': data['id'], "_model_type": data['_model_type'], "created": data['created'],
                     'dataset_id': data['dataset_id'], "name": data['name'], "notes_id": data['notes_id'],
                     'updated': data['updated'], "_id": data['_id'], "creator_id": data['creator_id'],
                     'meta_id': data['meta_id']})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
