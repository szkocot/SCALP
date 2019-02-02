from src.app.Model.Abstract.DbConnection import DbConnection


class Clinical(DbConnection):

    def __init__(self):
        super().__init__()
        self.id = None
        self.age_approx = None
        self.anatom_site_general = None
        self.benign_malignant = None
        self.diagnosis = None
        self.diagnosis_confirm_type = None
        self.melanocytic = None
        self.sex = None

    def getData(self, id):
        db = self.getConnection()
        cur = db.cursor()
        query = "SELECT id, age_approx, anatom_site_general, benign_malignant, diagnosis, diagnosis_confirm_type, melanocytic, sex FROM clinical WHERE id = %(id)s"
        cur.execute(query, {'id': id})
        result = cur.fetchone()

        self.id = result[0]
        self.age_approx = result[1]
        self.anatom_site_general = result[2]
        self.benign_malignant = result[3]
        self.diagnosis = result[3]
        self.diagnosis_confirm_type = result[3]
        self.melanocytic = result[3]
        self.sex = result[3]

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = "INSERT INTO clinical (id, age_approx, anatom_site_general, benign_malignant, diagnosis, diagnosis_confirm_type, melanocytic, sex)" \
                " VALUES (%(id)s, %(age_approx)s, %(anatom_site_general)s, %(benign_malignant)s, %(diagnosis)s, %(diagnosis_confirm_type)s, %(melanocytic)s, %(sex)s);"
        cur.execute(query, {'id': data['id'], "age_approx": data['age_approx'],
                            "anatom_site_general": data['anatom_site_general'],
                            "benign_malignant": data['benign_malignant'], "diagnosis": data['diagnosis'],
                            "diagnosis_confirm_type": data['diagnosis_confirm_type'],
                            "melanocytic": data['melanocytic'],
                            "sex": data['sex']})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]
