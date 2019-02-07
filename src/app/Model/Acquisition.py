from src.app.Model.Abstract.DbConnection import DbConnection


class Acquisition(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.image_type = None
        self.pixelsX = None
        self.pixelsY = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, image_type, pixelsX, pixelsY FROM acquisition WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()

        self.id = result[0]
        self.image_type = result[1]
        self.pixelsX = result[2]
        self.pixelsY = result[3]
        return self

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = 'INSERT INTO acquisition (image_type, "pixelsX", "pixelsY") VALUES (%(image_type)s, %(pixelsX)s, %(pixelsY)s);'
        cur.execute(query, {"image_type": data.get('image_type'), "pixelsX": data.get('pixelsX'),
                            "pixelsY": data.get('pixelsY')})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]

    def update(self):
        db = self.getConnection()
        cur = db.cursor()
        query = "UPDATE acquisition SET " \
                "image_type = %(image_type)s," \
                "pixelsX = %(pixelsX)s," \
                "pixelsY = %(pixelsY)s" \
                "WHERE id = %(id)s;"
        return cur.execute(query, {"image_type": self.image_type, "pixelsX": self.pixelsX,
                                   "pixelsY": self.pixelsY, 'id': self.id})
