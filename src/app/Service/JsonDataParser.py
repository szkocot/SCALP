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
        for element in meta:
            if element == "acquisition":
                acquisitionId = self.acquisition.insert(meta['acquisition'])
            elif element == 'clinical':
                clinicalId = self.clinical.insert(meta['clinical'])
            elif element == "unstructured":
                unstructuredId = self.unstructured.insert(meta['unstructured'])

        return self.meta.insert(
            {"acquisitionId": acquisitionId, "clinicalId": clinicalId, 'unstructuredId': unstructuredId})

    def parseTags(self, notes):
        tagIds = []
        for note in notes:
            tagIds.append(self.tag.insert(note))
        return tagIds

    def parseNotes(self, notes):
        for element in notes:
            if element == "reviewed":
                revievedId = self.reviewed.insert(notes['reviewed'])
            elif element == 'tags':
                tagIds = self.parseTags(notes['tags'])
        tagIds = ', '.join(map(str, tagIds))
        return self.notes.insert({'reviewedId': revievedId, 'tags': tagIds})

    def parseFile(self, metadata):
        for element in metadata:
            if element == '_id':
                continue
            elif element == '_modelType':
                continue
            elif element == 'created':
                continue
            elif element == 'creator':
                creatorId = self.creator.insert(metadata['creator'])
            elif element == 'dataset':
                datasetId = self.dataset.insert(metadata['dataset'])
            elif element == 'meta':
                metaId = self.parseMeta(metadata['meta'])
            elif element == 'name':
                continue
            elif element == 'notes':
                notesId = self.parseNotes(metadata['notes'])
            elif element == 'updated':
                continue
                #todo
        data = {"_model_type": metadata['_model_type'], "created": metadata['created'],
                'dataset_id': datasetId, "name": metadata['name'], "notes_id": notesId,
                'updated': metadata['updated'], "_id": metadata['_id'], "creator_id": creatorId,
                'meta_id': metaId}
        self.metadata.insert()

        return

    def getFileList(self):
        return os.listdir(self.path)

    def importFiles(self):
        for fileName in self.getFileList():
            metadata = json.load(open(self.path + "\\" + fileName))
            self.parseFile(metadata)
