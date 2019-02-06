#from src.app.Collection.BenignCollection import BenignCollection
#from src.app.Collection.MalignantCollection import MalignantCollection
from src.app.Collection.Abstract.Collection import Collection

class IsicCollection(Collection):

    def __init__(self):
        self.benignCollection = BenignCollection()
        self.malignantCollection = MalignantCollection()

