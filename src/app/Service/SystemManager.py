import config,psycopg2
from src.app.Model.System import System


class SystemManager():
    system = None
    dbVersion = None
    def __init__(self):
        self.system = System()

    def isDbSchemaCorrect(self):
        self.dbVersion = self.system.getDbVersion()
        if self.dbVersion == config.VERSION:
            return True
        else:
            return False

    def installSchema(self):
            self.system.initDB()

# each schema change needs dump into filename with upgraded version + new line here
    def upgradeSchema(self):
        self.system.updateDB('0.11')
        return

    def validate(self):
        while not self.isDbSchemaCorrect():
            if self.dbVersion is None:
                self.installSchema()

            elif self.dbVersion != config.VERSION:
                self.upgradeSchema()
