from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Reviewed import Reviewed


class ReviewedCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, accepted, \"userId\", \"time\" FROM public.reviewed ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()
            collection = []
            for row in result:
                reviewed = Reviewed()
                reviewed.id = row[0]
                reviewed.accepted = row[1]
                reviewed.userId = row[2]
                reviewed.time = row[3]
                collection.append(reviewed)
            self.collection = collection
        return self.collection
