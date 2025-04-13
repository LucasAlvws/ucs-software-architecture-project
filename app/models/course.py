from app.main import db


class Course(db.Model):
    __tablename__ = 'courses'
    __table_args__ = (db.UniqueConstraint('detailed_name', 'modality', 'degree', name='unique_course'),)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    detailed_name = db.Column(db.String(64))
    modality = db.Column(db.String(64))
    degree = db.Column(db.String(64))

    def __repr__(self):
        return f'{self.name} - {self.id}'
