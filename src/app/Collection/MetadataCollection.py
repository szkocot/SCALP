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

import os, config


class MetadataCollection(Collection):

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
        self.path = config.DATA_PATH
        self.dir = None

    def getCollection(self, where, offset=None, limit=None):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = """SELECT
                        m.id,
                        m._model_type,
                        m.created,
                        m.dataset_id,
                        m.name,
                        m.notes_id,
                        m.updated,
                        m._id,
                        m.creator_id,
                        m.meta_id,
                        m.image,
                        m.segmentation
                    FROM public.metadata m
                    INNER JOIN public.dataset d on m.dataset_id = d.id
                    INNER JOIN public.creator c ON c.id = m.creator_id
                    INNER JOIN public.meta meta ON meta.id = m.meta_id 
                    INNER JOIN public.acquisition a ON meta.acquisition_id = a.id
                    INNER JOIN public.clinical cl ON meta.clinical_id = cl.id
                    INNER JOIN public.unstructured u ON meta.unstructured_id = u.id"""
            if where != '' and where is not None:
                query += " WHERE " + where
            query += " ORDER BY m.id ASC"
            if offset is not None or limit is not None:
                query += " LIMIT " + str(limit) + " OFFSET " + str(offset) + ";"
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

    def parseMetadata(self, metadata):
        image = '\\static\\ISIC\\' + self.dir + "\\images\\" + metadata.get('name') + ".jpeg"
        try:
            segmentation = '\\static\\ISIC\\' + self.dir + "\\segmentation\\" + metadata.get('name') + "_expert.png"
            open(os.getcwd() + '\\src\\app' + segmentation, 'r')
        except Exception as e:
            try:
                segmentation = '\\static\\ISIC\\' + self.dir + "\\segmentation\\" + metadata.get('name') + "_novice.png"
                open(os.getcwd() + '\\src\\app' + segmentation, 'r')
            except Exception as e:
                print(e)
        creatorId = self.creator.insert(metadata.get('creator'))
        datasetId = self.dataset.insert(metadata.get('dataset'))
        metaId = self.parseMeta(metadata.get('meta'))
        notesId = self.parseNotes(metadata.get('notes'))
        data = {"_model_type": metadata.get('_modelType'), "created": metadata.get('created'),
                'dataset_id': datasetId, "name": metadata.get('name'), "notes_id": notesId,
                'updated': metadata.get('updated'), "_id": metadata.get('_id'), "creator_id": creatorId,
                'meta_id': metaId, 'image': image, 'segmentation': segmentation}
        return self.metadata.insert(data)
