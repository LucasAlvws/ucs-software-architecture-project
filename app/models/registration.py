from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship
from app.main import db

class Registration(db.Model):
    __tablename__ = 'registrations'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(32))
    city = db.Column(db.String(32))
    year = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer())

    institution_id = db.Column(db.Integer, ForeignKey('institutions.id'), nullable=False)
    course_id = db.Column(db.Integer, ForeignKey('courses.id'), nullable=False)

    institution = relationship('Institution', backref='registrations')
    course = relationship('course', backref='registrations')

    def __repr__(self):
        return f'{self.course.name} - {self.year}'