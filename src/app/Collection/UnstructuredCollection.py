from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Unstructured import Unstructured


class UnstructuredCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, diagnosis, id1, localization, site FROM public.unstructured ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()
            collection = []
            for row in result:
                unstructured = Unstructured()
                unstructured.id = row[0]
                unstructured.diagnosis = row[1]
                unstructured.id1 = row[2]
                unstructured.localization = row[3]
                unstructured.site = row[4]
                collection.append(unstructured)
            self.collection = collection
        return self.collection
