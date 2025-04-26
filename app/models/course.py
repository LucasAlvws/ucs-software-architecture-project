from app.main import db


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    detailed_name = db.Column(db.String(64))
    modality = db.Column(db.String(64))
    degree = db.Column(db.String(64))

    def __repr__(self):
        return f'{self.name} - {self.id}'
