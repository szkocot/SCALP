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

import os, json, config


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
        self.path = config.DATA_PATH
        self.dir = None

    def setBaseDir(self, dir):
        self.dir = dir

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
        image = self.path + self.dir + "\\images\\" + metadata.get('name') + ".jpeg"
        try:
            segmentation = self.path + self.dir + "\\segmentation\\" + metadata.get('name') + "_expert.png"
            open(segmentation, 'r')
        except Exception as e:
            try:
                segmentation = self.path + self.dir + "\\segmentation\\" + metadata.get('name') + "_novice.png"
                open(segmentation)
            except Exception as e:
                print (e)
        creatorId = self.creator.insert(metadata.get('creator'))
        datasetId = self.dataset.insert(metadata.get('dataset'))
        metaId = self.parseMeta(metadata.get('meta'))
        notesId = self.parseNotes(metadata.get('notes'))
        data = {"_model_type": metadata.get('_modelType'), "created": metadata.get('created'),
                'dataset_id': datasetId, "name": metadata.get('name'), "notes_id": notesId,
                'updated': metadata.get('updated'), "_id": metadata.get('_id'), "creator_id": creatorId,
                'meta_id': metaId,'image': image,'segmentation': segmentation}
        return self.metadata.insert(data)

    def getFileList(self):
        return os.listdir(self.path + self.dir + "\\description")

    def importFiles(self, catalog):
        insertedIDs = []
        self.setBaseDir(catalog)
        for fileName in self.getFileList():
            path = self.path + self.dir + "\\description\\" + fileName
            metadata = json.load(open(path))
            insertedIDs.append(self.parseFile(metadata))

        print(insertedIDs)
