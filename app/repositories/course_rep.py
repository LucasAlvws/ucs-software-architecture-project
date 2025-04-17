from app.dao import CourseDao
from app.models import Course
from app.repositories.base_rep import BaseRepository


class CourseRepository(BaseRepository):
    def __init__(self):
        self.dao = CourseDao()
        self.model = Course

    def filter_unique(self, detailed_name, modality, degree, **_):
        defaults = {'detailed_name': detailed_name, 'modality': modality, 'degree': degree}
        return self.dao.get_by_attributes(defaults)