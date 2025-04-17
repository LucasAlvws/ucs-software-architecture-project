from app.dao import InstitutionDao
from app.models import Institution
from app.repositories.base_rep import BaseRepository


class InstitutionRepository(BaseRepository):
    def __init__(self):
        self.dao = InstitutionDao()
        self.model = Institution

    def filter_unique(self, name, organization, category, **_):
        defaults = {'name': name, 'organization': organization, 'category': category}
        return self.dao.get_by_attributes(defaults)