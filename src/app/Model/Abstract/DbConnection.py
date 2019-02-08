import psycopg2
import config


class DbConnection:

    def __init__(self):
        return

    def getConnection(self):
        connection = None
        try:
            _host = config.DATABASE_CONFIG['host']
            _port = config.DATABASE_CONFIG['port']
            _db = config.DATABASE_CONFIG['dbname']
            _user = config.DATABASE_CONFIG['user']
            _password = config.DATABASE_CONFIG['password']
            connection = psycopg2.connect(host=_host,
                                          user=_user,
                                          password=_password,
                                          dbname=_db)
            connection.autocommit = True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return connection
