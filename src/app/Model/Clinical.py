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
        query = """"SELECT id, age_approx, anatom_site_general, benign_malignant, diagnosis, diagnosis_confirm_type, melanocytic, sex
                FROM public.clinical WHERE id = %(id)s"""
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
        return self

    def insert(self, data):
        db = self.getConnection()
        cur = db.cursor()
        query = """INSERT INTO public.clinical (age_approx, anatom_site_general, benign_malignant, diagnosis, diagnosis_confirm_type, melanocytic, sex)
                 VALUES (%(age_approx)s, %(anatom_site_general)s, %(benign_malignant)s, %(diagnosis)s, %(diagnosis_confirm_type)s, %(melanocytic)s, %(sex)s);"""
        cur.execute(query,
                    {"age_approx": data.get('age_approx'), "anatom_site_general": data.get('anatom_site_general'),
                     "benign_malignant": data.get('benign_malignant'), "diagnosis": data.get('diagnosis'),
                     "diagnosis_confirm_type": data.get('diagnosis_confirm_type'),
                     "melanocytic": data.get('melanocytic'), "sex": data.get('sex')})
        cur.execute('SELECT LASTVAL()')
        return cur.fetchone()[0]

    def update(self):
        db = self.getConnection()
        cur = db.cursor()
        query = """UPDATE public.clinical SET
                age_approx = %(age_approx)s,
                anatom_site_general = %(anatom_site_general)s,
                benign_malignant = %(benign_malignant)s,
                diagnosis = %(diagnosis)s,
                diagnosis_confirm_type =%(diagnosis_confirm_type)s,
                melanocytic =%(melanocytic)s,
                sex = %(sex)s
                WHERE id = %(id)s"""
        cur.execute(query,
                    {"age_approx": self.age_approx, "anatom_site_general": self.anatom_site_general,
                     "benign_malignant": self.benign_malignant, "diagnosis": self.diagnosis,
                     "diagnosis_confirm_type": self.diagnosis_confirm_type,
                     "melanocytic": self.melanocytic, "sex": self.sex, 'id': self.id})
