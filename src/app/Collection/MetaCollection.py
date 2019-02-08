from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Meta import Meta


class MetaCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, acquisition_id, clinical_id, unstructured_id FROM meta ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()
            collection = []
            for row in result:
                meta = Meta()
                meta.id = row[0]
                meta.acquisition_id = row[1]
                meta.clinical_id = row[2]
                meta.unstructured_id = row[3]
                collection.append(meta)
            self.collection = collection
        return self.collection
