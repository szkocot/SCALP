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
from src.app.Model.Isic import Isic
import os


class IsicCollection(Collection):

    def __init__(self):
        super().__init__()
        self.acquisition = AcquisitionCollection().getCollection()
        self.clinical = ClinicalCollection().getCollection()
        self.creator = CreatorCollection().getCollection()
        self.dataset = DatasetCollection().getCollection()
        self.meta = MetaCollection().getCollection()
        self.metadata = MetadataCollection()
        self.tag = TagCollection().getCollection()
        self.notes = NotesCollection().getCollection()
        self.unstructured = UnstructuredCollection().getCollection()
        self.reviewed = ReviewedCollection().getCollection()
        self.parser = JsonDataParser()
        self.collection = None
        self.where = None

    # todo i assume we are inserting same data struct as the one we take from json
    def insert(self, data):
        return MetadataCollection().parseMetadata(data)

    def getCollection(self, offset, limit):
        if self.collection is None or self.where == '':
            collection = []
            for row in self.metadata.getCollection(self.where, offset, limit):
                isic = Isic()
                isic.id = row.id
                isic._model_type = row._model_type
                isic.created = row.created
                isic.dataset_id = self.getDatasetById(row.dataset_id)
                isic.name = row.name
                isic.notes = self.getNotesById(row.notes_id)
                isic.updated = row.updated
                isic._id = row._id
                isic.creator = self.getCreatorById(row.creator_id)
                isic.meta = self.getMetaById(row.meta_id)
                isic.image = row.image
                isic.segmentation = row.segmentation
                collection.append(isic)
            self.collection = collection
        return self.collection

    def getNotesById(self, id):
        for note in self.notes:
            if id is not None and id == note.id:
                note.reviewed = self.getReviewedById(note.reviewedId)
                note.tags = self.getTagsByIds(note.tags)
                return note
        return None

    def getReviewedById(self, id):
        for reviewed in self.reviewed:
            if id is not None and id == reviewed.id:
                return reviewed
        return None

    def getTagsByIds(self, id):
        out = []
        if id is '':
            return None
        ids = id.split(', ')
        for id in ids:
            id = int(id)
            for tag in self.tag:
                if id is not None and id == tag.id:
                    out.append(tag)
                    break
        return out

    def getCreatorById(self, id):
        for creator in self.creator:
            if id is not None and id == creator.id:
                return creator
        return None

    def getMetaById(self, id):
        for meta in self.meta:
            if id is not None and id == meta.id:
                outMeta = Meta()
                for acq in self.acquisition:
                    if meta.acquisition_id == acq.id:
                        outMeta.acquisition = acq
                        break
                for cli in self.clinical:
                    if meta.clinical_id == cli.id:
                        outMeta.clinical = cli
                        break
                for unstr in self.unstructured:
                    if meta.unstructured_id == unstr.id:
                        outMeta.unstructured = unstr
                        break
                del outMeta.unstructured_id
                del outMeta.acquisition_id
                del outMeta.clinical_id
                outMeta.id = meta.id
                return outMeta
        return None

    def getDatasetById(self, id):
        for dataset in self.dataset:
            if id is not None and id == dataset.id:
                return dataset

    def parseFilters(self, filters):
        sql = ''
        i = 0
        for key, val in filters.items():
            if val is not '':
                if i == 0:
                    if key == 'cl.age_approx' and val != '' and val.isdigit():
                        sql = key + " =" + val + " "
                    elif val != '' and key != 'cl.age_approx' and key != 'cl.sex':
                        sql = key + " ilike '%" + val + "%' "
                    elif val != '' and key == 'cl.sex':
                        sql = key + " = '" + val + "' "
                    i += 1
                else:
                    if key == 'cl.age_approx' and val != '' and val.isdigit():
                        sql += " AND " + key + " =" + val + " "
                    elif val != '' and key != 'cl.age_approx' and key != 'cl.sex':
                        sql += " AND " + key + " ilike '%" + val + "%' "
                    elif val != '' and key == 'cl.sex':
                        sql += " AND " + key + " = '" + val + "' "
        self.where = sql
        return

    def getPages(self, limit):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT count(id) FROM public.metadata"
        cur.execute(query)
        result = cur.fetchone()
        return int(int(result[0]) / limit)

    def getMetadataById(self, id):

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
                    WHERE m.id = %(id)s;"""
        db = self.getConnection()
        cur = db.cursor()
        cur.execute(query, {'id': id})
        row = cur.fetchone()
        isic = Isic()
        isic.id = row[0]
        isic._model_type = row[1]
        isic.created = row[2]
        isic.dataset = self.getDatasetById(row[3])
        isic.name = row[4]
        isic.notes = self.getNotesById(row[5])
        isic.updated = row[6]
        isic._id = row[7]
        isic.creator = self.getCreatorById(row[8])
        isic.meta = self.getMetaById(row[9])
        isic.image = row[10].replace('\\', '/')
        isic.segmentation = row[11].replace('\\', '/')
        return isic
