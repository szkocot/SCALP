from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Creator import Creator


class CreatorCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, _id, name FROM creator ORDER BY id ASC"
            cur.execute(query, {'id': id})
            result = cur.fetchall()
            collection = []
            for row in result:
                creator = Creator()
                creator.id = row[0]
                creator._id = row[1]
                creator.name = row[2]
                collection.append(creator)
            self.collection = collection
        return self.collection
