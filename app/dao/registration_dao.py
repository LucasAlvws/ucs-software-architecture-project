from app.models import Registration
from app.dao.base_dao import BaseDao


class RegistrationDao(BaseDao):
    def __init__(self):
        self.model = Registration
