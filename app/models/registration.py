from app.main import db


class Registration(db.Model):
    __tablename__ = 'registration'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(32))
    city = db.Column(db.String(32))
    year = db.Column(db.Integer())
    student_count = db.Column(db.Integer())
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
