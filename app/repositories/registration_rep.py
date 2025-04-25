from app.dao import RegistrationDao
from app.models import Registration
from app.repositories.base_rep import BaseRepository


class RegistrationRepository(BaseRepository):
    def __init__(self):
        self.dao = RegistrationDao()
        self.model = Registration

    def filter_unique(self, institution, course, **_):
        defaults = {'institution': institution, 'course': course}
        return self.dao.get_by_attributes(defaults)
    
    def bulk_save_objects(self, registration_list):
        self.dao.bulk_save_objects(registration_list)

    def create_obj(self, defaults):
        return self.model(**defaults)