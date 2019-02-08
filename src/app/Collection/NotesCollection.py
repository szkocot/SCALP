from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Notes import Notes


class NotesCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, reviewed_id, tags FROM notes ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()
            collection = []
            for row in result:
                notes = Notes()
                notes.id = row[0]
                notes.reviewedId = row[1]
                notes.tags = row[2]
                collection.append(notes)
            self.collection = collection
        return self.collection
