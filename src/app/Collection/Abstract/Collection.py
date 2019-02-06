class Collection:

    def __init__(self):
        self.limit = 20
        self.offset = 0
        self.field = None
        self.value = None

    def setLimit(self, limit):
        self.limit = limit

    def setOffset(self, offset):
        self.offset = offset

    def setFilter(self, field, value):
        self.field = field
        self.value = value

    def getCollection(self):
        return None
