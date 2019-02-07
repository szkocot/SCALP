from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Metadata import Metadata


class MetadataCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, _model_type, created, dataset_id, name, notes_id, updated, _id, creator_id, meta_id, image, segmentation FROM metadata ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()
            collection = []
            for row in result:
                metadata = Metadata()
                metadata.id = row[0]
                metadata._model_type = row[1]
                metadata.created = row[2]
                metadata.dataset_id = row[3]
                metadata.name = row[4]
                metadata.notes_id = row[5]
                metadata.updated = row[6]
                metadata._id = row[7]
                metadata.creator_id = row[8]
                metadata.meta_id = row[9]
                metadata.image = row[10]
                metadata.segmentation = row[11]
                collection.append(metadata)
            self.collection = collection


        return self.collection
