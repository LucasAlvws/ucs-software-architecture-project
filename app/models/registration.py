from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
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

    institution_id = db.Column(db.Integer, ForeignKey('institutions.id'), nullable=False)
    course_id = db.Column(db.Integer, ForeignKey('courses.id'), nullable=False)

    institution = relationship('Institution', backref='registrations')
    course = relationship('Course', backref='registrations')

    def __repr__(self):
        return f'{self.course.name} - {self.state} - {self.city}'
