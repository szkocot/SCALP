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


class BenignCollection(Collection):

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

    def getCollection(self):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, __model_type, _created, dataset_id, name, notes_id, updated, _id, creator_id, meta_id, image, segmentation FROM metadata WHERE "
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
        return self