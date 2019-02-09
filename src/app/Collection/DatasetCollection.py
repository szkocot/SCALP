from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Dataset import Dataset


class DatasetCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, _access_level, _id, description, license, name, updated FROM public.dataset ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()
            collection = []
            for row in result:
                dataset = Dataset()
                dataset.id = row[0]
                dataset._access_level = row[1]
                dataset._id = row[2]
                dataset.description = row[3]
                dataset.license = row[4]
                dataset.name = row[5]
                dataset.updated = row[6]
                collection.append(dataset)
            self.collection = collection
        return self.collection
