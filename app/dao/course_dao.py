from app.models import Course
from app.main import db


class CourseDao:
    def get_by_id(self, course_id):
        return Course.query.get(course_id)

    def save(self, course):
        db.session.add(course)
        db.session.commit()

    def delete(self, course):
        db.session.delete(course)
        db.session.commit()
