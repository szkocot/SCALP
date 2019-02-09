import config
from src.app.Model.System import System
from src.app.Service.JsonDataParser import JsonDataParser


class SystemManager():

    def __init__(self):
        self.system = System()
        self.jsons = JsonDataParser()

    def isDbSchemaCorrect(self):
        self.dbVersion = self.system.getDbVersion()
        if self.dbVersion == config.VERSION:
            return True
        else:
            return False

    def installSchema(self):
        self.system.initDB()

    def upgradeSchema(self):
        return

    def validate(self):
        imported = False
        while not self.isDbSchemaCorrect():
            if self.dbVersion is None:
                self.installSchema()
            elif self.dbVersion != config.VERSION:
                self.upgradeSchema()
            if config.IMPORT == "json" and imported is False:
                self.jsonsCall()
                imported = True

    def jsonsCall(self):
        self.jsons.importFiles('malignant')
        self.jsons.importFiles('benign')
