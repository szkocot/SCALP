from src.app.Model.Abstract.DbConnection import DbConnection


class Isic(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self._model_type = None
        self.created = None
        self.name = None
        self.notes_id = None
        self.updated = None
        self.image = None
        self.segmentation = None
