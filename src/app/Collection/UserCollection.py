from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.User import User


class UserCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, username, name, surname, email, admin FROM users ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()
            collection = []
            for row in result:
                user = User()
                user.id = row[0]
                user.username = row[1]
                user.name = row[2]
                user.surname = row[3]
                user.email = row[4]
                user.admin = row[5]
                collection.append(user)
            self.collection = collection
        return self.collection
