from app.models import Course
from app.dao.base_dao import BaseDao


class CourseDao(BaseDao):
    def __init__(self):
        self.model = Course
