from src.app.Collection.Abstract.Collection import Collection
from src.app.Collection.AcquisitionCollection import AcquisitionCollection, Acquisition
from src.app.Collection.ClinicalCollection import ClinicalCollection, Clinical
from src.app.Collection.CreatorCollection import CreatorCollection, Creator
from src.app.Collection.DatasetCollection import DatasetCollection, Dataset
from src.app.Collection.MetaCollection import MetaCollection, Meta
from src.app.Collection.MetadataCollection import MetadataCollection, Metadata
from src.app.Collection.NotesCollection import NotesCollection, Notes
from src.app.Collection.ReviewedCollection import ReviewedCollection, Reviewed
from src.app.Collection.TagCollection import TagCollection, Tag
from src.app.Collection.UnstructuredCollection import UnstructuredCollection, Unstructured
from src.app.Service.JsonDataParser import JsonDataParser


class IsicCollection(Collection):

    def __init__(self):
        super().__init__()
        self.acquisition = AcquisitionCollection().getCollection()
        self.clinical = ClinicalCollection().getCollection()
        self.creator = CreatorCollection().getCollection()
        self.dataset = DatasetCollection().getCollection()
        self.meta = MetaCollection().getCollection()
        self.metadata = MetadataCollection().getCollection()
        self.tag = TagCollection().getCollection()
        self.notes = NotesCollection().getCollection()
        self.unstructured = UnstructuredCollection().getCollection()
        self.reviewed = ReviewedCollection().getCollection()
        self.parser = JsonDataParser()
        self.collection = None

    # todo i assume we are inserting same data struct as the one we take from json
    def insert(self, data):
        return MetadataCollection().parseMetadata(data)

    # todo fetch whole object not ids
    def getCollection(self):
        if self.collection is None:
            collection = []
            for row in self.metadata:
                metadata = Metadata()
                self.id = row[0]
                self._model_type = row[1]
                self.created = row[2]
                self.dataset_id = row[3]
                self.name = row[4]
                self.notes_id = row[5]
                self.updated = row[6]
                self._id = row[7]
                self.creator_id = row[8]
                self.meta_id = row[9]
                self.image = row[10]
                self.segmentation = row[11]

            collection.append(metadata)
        return self.collection
