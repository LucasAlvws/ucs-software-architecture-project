from app.dao import InstitutionDao
from app.models import Institution
from app.repositories.base_rep import BaseRepository


class InstitutionRepository(BaseRepository):
    def __init__(self):
        self.dao = InstitutionDao()
        self.model = Institution
