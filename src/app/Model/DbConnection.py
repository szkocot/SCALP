import psycopg2


class DbConnection:
    _host = ''
    _port = ''
    _user = ''
    _password = ''
    _db = ''
    connection = None

    def __init__(self):
        _host = "127.0.0.1"
        _port = 5432
        _db = "bbd"
        _user = "postgres"
        _password = "psql"

    def getConnection(self):
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(host=self._host,
                                                   user=self._user,
                                                   password=self._password,
                                                   dbname=self._db)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        return self.connection

    def getCursor(self):
        connection = self.getConnection()
        return connection.cursor()

    def __del__(self):
        self.connection = None
