from src.app.Model.Acquisition import Acquisition
from src.app.Model.Clinical import Clinical
from src.app.Model.Creator import Creator
from src.app.Model.Dataset import Dataset
from src.app.Model.Meta import Meta
from src.app.Model.Metadata import Metadata
from src.app.Model.Notes import Notes
from src.app.Model.Reviewed import Reviewed
from src.app.Model.Tags import Tags
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
        self.tags = Tags()
        self.notes = Notes()
        self.unstructured = Unstructured()
        self.reviewed = Reviewed()
        self.data = None
        self.path = None
        return

    def setPath(self, path):
        self.path = path

    def parseMeta(self,meta):
        return

    def parseTags(self, notes):
        for note in notes:
            self.notes.insert(note)

    def parseNotes(self,notes):
        for element in notes:
            if element == "reviewed":
                self.reviewed.insert(notes['reviewed'])
            elif element == 'tags':
                self.parseTags(notes['tags'])
        return

    # todo here we need the magic to happen
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
        data = { "_model_type": metadata['_model_type'], "created": metadata['created'],
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
