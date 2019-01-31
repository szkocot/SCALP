import psycopg2
import config


class DbConnection:
    _host = ''
    _port = ''
    _user = ''
    _password = ''
    _db = ''
    connection = None

    def __init__(self):
        _host = config.DATABASE_CONFIG['host']
        _port = config.DATABASE_CONFIG['port']
        _db = config.DATABASE_CONFIG['dbname']
        _user = config.DATABASE_CONFIG['user']
        _password = config.DATABASE_CONFIG['password']

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

    def initDB(self):
        #todo auto import db if doesnt exsist
        return
