from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Tag import Tag


class TagCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, data FROM public.tag ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()
            collection = []
            for row in result:
                tag = Tag()
                tag.id = row[0]
                tag.data = row[1]
                collection.append(tag)
            self.collection = collection
        return self.collection
