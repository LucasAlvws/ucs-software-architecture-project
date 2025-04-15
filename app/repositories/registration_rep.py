from app.dao import RegistrationDao
from app.models import Registration
from app.repositories.base_rep import BaseRepository


class RegistrationRepository(BaseRepository):
    def __init__(self):
        self.dao = RegistrationDao()
        self.model = Registration
