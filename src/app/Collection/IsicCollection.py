from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Acquisition import Acquisition
from src.app.Model.Clinical import Clinical
from src.app.Model.Creator import Creator
from src.app.Model.Dataset import Dataset
from src.app.Model.Meta import Meta
from src.app.Model.Metadata import Metadata
from src.app.Model.Notes import Notes
from src.app.Model.Reviewed import Reviewed
from src.app.Model.Tag import Tag
from src.app.Model.Unstructured import Unstructured
from src.app.Service.JsonDataParser import JsonDataParser


class IsicCollection(Collection):

    def __init__(self):
        super().__init__()
        self.acquisition = Acquisition()
        self.clinical = Clinical()
        self.creator = Creator()
        self.dataset = Dataset()
        self.meta = Meta()
        self.metadata = Metadata()
        self.tag = Tag()
        self.notes = Notes()
        self.unstructured = Unstructured()
        self.reviewed = Reviewed()
        self.parser = JsonDataParser()

    # todo
    def insert(self, data):
        creatorId = self.creator.insert(data.get('creator'))
        datasetId = self.dataset.insert(data.get('dataset'))
        metaId = self.parser.parseMeta(data.get('meta'))
        notesId = self.parser.parseNotes(data.get('notes'))
        data = {"_model_type": data.get('_modelType'), "created": data.get('created'),
                'dataset_id': datasetId, "name": data.get('name'), "notes_id": notesId,
                'updated': data.get('updated'), "_id": data.get('_id'), "creator_id": creatorId,
                'meta_id': metaId, 'image': data['image'], 'segmentation': data['segmentation']}
        return self.metadata.insert(data)

    # todo fetch whole object not ids
    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, __model_type, _created, dataset_id, name, notes_id, updated, _id, creator_id, meta_id, image, segmentation FROM metadata ORDER BY id ASC"
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
                collection.append(metadata)
            self.collection = collection
        return self.collection
