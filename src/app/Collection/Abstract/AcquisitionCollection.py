from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Acquisition import Acquisition


class AcquisitionCollection(Collection):

    def __init__(self):
        super().__init__()
        self.collection = None

    def getUserCollection(self):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, image_type, pixelsX, pixelsY FROM acquisition ORDER BY id ASC"
        cur.execute(query)
        result = cur.fetchall()

        collection = []
        for row in result:
            acquisition = Acquisition()
            acquisition.id = row[0]
            acquisition.image_type = row[1]
            acquisition.pixelsX = row[2]
            acquisition.pixelsY = row[3]
            collection.append(acquisition)
        return collection
