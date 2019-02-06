from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.User import User


class UserCollection(Collection):

    def __init__(self):
        super().__init__()

    def getUserCollection(self):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, username, name, surname, email, admin FROM users ORDER BY id ASC"
        cur.execute(query)
        result = cur.fetchall()

        collection = []
        for row in result:
            user = User()

