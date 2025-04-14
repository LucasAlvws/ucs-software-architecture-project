from app.dao import InstitutionDao
from app.models import Institution


class InstitutionRepository:
    def __init__(self):
        self.dao = InstitutionDao()

    def update_or_create(self, defaults):
        institution = Institution(**defaults)
        self.dao.save(institution)
        return institution
