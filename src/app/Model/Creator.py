from src.app.Model.Abstract.DbConnection import DbConnection


class Creator(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self._id = None
        self.name = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, _id, \"name\" FROM public.creator WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()

        self.id = result[0]
        self._id = result[1]
        self.name = result[2]
        return self

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO public.creator (_id, \"name\")" \
                " VALUES (%(_id)s, %(name)s);"
        cur.execute(query, {"_id": data.get('_id'), "name": data.get('name')})
        cur.execute('SELECT LASTVAL()')
        result = cur.fetchone()
        return result[0]

    def update(self):
        db = self.getConnection()
        cur = db.cursor()
        query = "UPDATE public.creator SET _id = %(_id)s, \"name\"= %(name)s WHERE id = %(id)s;"
        cur.execute(query, {"_id": self._id, "name": self.name, 'id': self.id})
