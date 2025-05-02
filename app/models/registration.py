from app.main import db


class Registration(db.Model):
    __tablename__ = 'registrations'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(32))
    city = db.Column(db.String(32))
    year_2014 = db.Column(db.Integer())
    year_2015 = db.Column(db.Integer())
    year_2016 = db.Column(db.Integer())
    year_2017 = db.Column(db.Integer())
    year_2018 = db.Column(db.Integer())
    year_2019 = db.Column(db.Integer())
    year_2020 = db.Column(db.Integer())
    year_2021 = db.Column(db.Integer())
    year_2022 = db.Column(db.Integer())
    institution_name = db.Column(db.String(128))
    institution_acronym = db.Column(db.String(64))
    institution_organization = db.Column(db.String(64))
    institution_category = db.Column(db.String(64))
    course_name = db.Column(db.String(64))
    course_detailed_name = db.Column(db.String(64))
    course_modality = db.Column(db.String(64))
    course_degree = db.Column(db.String(64))
    

    def __repr__(self):
        return f'{self.institution_name} - {self.course_detailed_name}'
