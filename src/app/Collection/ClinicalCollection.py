from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Clinical import Clinical


class ClinicalCollection(Collection):

    def __init__(self):
        super().__init__()

    def getUserCollection(self):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, age_approx, anatom_site_general, benign_malignant, diagnosis, diagnosis_confirm_type, melanocytic, sex FROM clinical ORDER BY id ASC"
        cur.execute(query)
        result = cur.fetchall()

        collection = []
        for row in result:
            clinical = Clinical()
            self.id = row[0]
            self.age_approx = row[1]
            self.anatom_site_general = row[2]
            self.benign_malignant = row[3]
            self.diagnosis = row[4]
            self.diagnosis_confirm_type = row[5]
            self.melanocytic = row[6]
            self.sex = row[7]
            collection.append(clinical)
        return collection
