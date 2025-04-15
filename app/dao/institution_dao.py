from app.models import Institution
from app.dao.base_dao import BaseDao


class InstitutionDao(BaseDao):
    def __init__(self):
        self.model = Institution
