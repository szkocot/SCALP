import psycopg2
import config


class DbConnection:

    def __init__(self):
        self.connection = None

    def getConnection(self):
        try:
            _host = config.DATABASE_CONFIG['host']
            _port = config.DATABASE_CONFIG['port']
            _db = config.DATABASE_CONFIG['dbname']
            _user = config.DATABASE_CONFIG['user']
            _password = config.DATABASE_CONFIG['password']
            self.connection = psycopg2.connect(host=_host,
                                           user=_user,
                                           password=_password,
                                           dbname=_db)
            self.connection.autocommit = True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return self.connection

    def __del__(self):
        self.connection = None
