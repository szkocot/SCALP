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

import os, json


class JsonDataParser:

    def __init__(self):
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
        self.data = None
        self.path = None
        return

    def setPath(self, path):
        self.path = path

    def parseMeta(self, meta):
        acquisitionId = self.acquisition.insert(meta.get('acquisition'))
        clinicalId = self.clinical.insert(meta.get('clinical'))
        unstructuredId = self.unstructured.insert(meta.get('unstructured'))
        return self.meta.insert(
            {"acquisitionId": acquisitionId, "clinicalId": clinicalId, 'unstructuredId': unstructuredId})

    def parseTags(self, notes):
        tagIds = []
        for note in notes:
            tagIds.append(self.tag.insert(note))
        return tagIds

    def parseNotes(self, notes):
        revievedId = self.reviewed.insert(notes.get('reviewed'))
        tagIds = self.parseTags(notes.get('tags'))
        tagIds = ', '.join(map(str, tagIds))
        return self.notes.insert({'reviewedId': revievedId, 'tags': tagIds})

    def parseFile(self, metadata):
        creatorId = self.creator.insert(metadata.get('creator'))
        datasetId = self.dataset.insert(metadata.get('dataset'))
        metaId = self.parseMeta(metadata.get('meta'))
        notesId = self.parseNotes(metadata.get('notes'))
        data = {"_model_type": metadata.get('_modelType'), "created": metadata.get('created'),
                'dataset_id': datasetId, "name": metadata.get('name'), "notes_id": notesId,
                'updated': metadata.get('updated'), "_id": metadata.get('_id'), "creator_id": creatorId,
                'meta_id': metaId}
        return self.metadata.insert(data)

    def getFileList(self):
        return os.listdir(self.path)

    def importFiles(self):
        insertedIDs = []
        for fileName in self.getFileList():
            metadata = json.load(open(self.path + "\\" + fileName))
            insertedIDs.append(self.parseFile(metadata))

        print(insertedIDs)
