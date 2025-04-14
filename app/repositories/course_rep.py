from app.dao import CourseDao
from app.models import Course


class CourseRepository:
    def __init__(self):
        self.dao = CourseDao()

    def update_or_create(self, defaults):
        course = Course(**defaults)
        self.dao.save(course)
        return course
