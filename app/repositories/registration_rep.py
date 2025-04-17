from app.dao import RegistrationDao
from app.models import Registration
from app.repositories.base_rep import BaseRepository


class RegistrationRepository(BaseRepository):
    def __init__(self):
        self.dao = RegistrationDao()
        self.model = Registration

    def filter_unique(self, institution, course, year, **_):
        defaults = {'institution': institution, 'course': course, 'year': year}
        return self.dao.get_by_attributes(defaults)
