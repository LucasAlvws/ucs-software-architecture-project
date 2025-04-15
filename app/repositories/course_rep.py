from app.dao import CourseDao
from app.models import Course
from app.repositories.base_rep import BaseRepository


class CourseRepository(BaseRepository):
    def __init__(self):
        self.dao = CourseDao()
        self.model = Course
