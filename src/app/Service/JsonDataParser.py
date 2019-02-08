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
from src.app.Collection.MetadataCollection import MetadataCollection
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
        self.collection = MetadataCollection()

    def setBaseDir(self, dir):
        self.dir = dir



    def getFileList(self):
        return os.listdir(self.path + self.dir + "\\description")

    def importFiles(self, catalog):
        insertedIDs = []
        self.setBaseDir(catalog)
        self.collection.dir = catalog
        for fileName in self.getFileList():
            path = self.path + self.dir + "\\description\\" + fileName
            metadata = json.load(open(path))
            insertedIDs.append(self.collection.parseMetadata(metadata))

        print(insertedIDs)
