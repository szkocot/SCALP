import os
from src.app.Model.Abstract.DbConnection import DbConnection
import config, psycopg2


class System(DbConnection):

    def __init__(self):
        super().__init__()

    def initDB(self):
        try:
            db = self.getConnection()
            cur = db.cursor()
            cur.execute(open(os.path.join(config.BASE_DIR, config.DUMP_FILE_PATH, "dump.sql"), "r").read())
            db.close()
        except (Exception, psycopg2.DatabaseError) as error:
            db.rollback()
            return print(error)
        db = self.getConnection()
        cur = db.cursor()
        cur.execute("INSERT INTO public.app_version (ver) VALUES (0.1);")
        return

    def updateDB(self, version):
        db = self.getConnection()
        cur = db.cursor()
        try:
            cur.execute(open(os.path.join(config.BASE_DIR, config.DUMP_FILE_PATH, version + ".sql"), "r").read())
            query = "INSERT INTO public.app_version (ver) VALUES (%(version)s);"
            cur.execute(query, {'version': version})
        except (Exception, psycopg2.DatabaseError) as error:
            db.rollback()
            print(error)
        return

    def getDbVersion(self):
        db = self.getConnection()
        cur = db.cursor()
        try:
            query = "SELECT ver FROM public.app_version ORDER BY id DESC;"
            cur.execute(query)
            result = cur.fetchone()
            result = result[0]
        except (Exception, psycopg2.DatabaseError) as error:
            result = None
            db.rollback()
            print(str(error) + "\nno tables detected...\ncreating tables and setting the db relations")
        return result
