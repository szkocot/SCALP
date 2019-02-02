from src.app.Model.Abstract.DbConnection import DbConnection


class UserCollection(DbConnection):

    def __init__(self):
        super().__init__()


    def getUserCollection(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, username, name, surname, email, admin FROM users"
        result = cur.execute(query)
        return result

