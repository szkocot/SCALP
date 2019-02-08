from src.app.Collection.Abstract.Collection import Collection
from src.app.Model.Clinical import Clinical


class ClinicalCollection(Collection):

    def __init__(self):
        super().__init__()

    def getCollection(self):
        if self.collection is None:
            db = self.getConnection()
            cur = db.cursor()
            query = "SELECT id, age_approx, anatom_site_general, benign_malignant, diagnosis, diagnosis_confirm_type, melanocytic, sex FROM clinical ORDER BY id ASC"
            cur.execute(query)
            result = cur.fetchall()

            collection = []
            for row in result:
                clinical = Clinical()
                clinical.id = row[0]
                clinical.age_approx = row[1]
                clinical.anatom_site_general = row[2]
                clinical.benign_malignant = row[3]
                clinical.diagnosis = row[4]
                clinical.diagnosis_confirm_type = row[5]
                clinical.melanocytic = row[6]
                clinical.sex = row[7]
                collection.append(clinical)
            self.collection = collection
        return self.collection
