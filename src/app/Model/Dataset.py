from src.app.Model.Abstract.DbConnection import DbConnection


class Dataset(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self._access_level = None
        self._id = None
        self.description = None
        self.license = None
        self.name = None
        self.updated = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, _access_level, _id, description, license, name, updated FROM dataset WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()
        self.id = result[0]
        self._access_level = result[1]
        self._id = result[2]
        self.description = result[3]
        self.license = result[4]
        self.name = result[5]
        self.updated = result[6]

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO dataset (id, _access_level, _id, description, license, name, updated)" \
                " VALUES (%(id)s, %(_access_level)s, %(_id)s, %(description)s, %(license)s, %(name)s, %(updated)s);"
        cur.execute(query, {'id': data['id'], "_access_level": data['_access_level'], "_id": data['_id'],
                            'description': data['description'], "license": data['license'], "name": data['name'],
                            'updated': data['updated'], })
        return
