from app.dao import RegistrationDao
from app.models import Registration


class RegistrationRepository:
    def __init__(self):
        self.dao = RegistrationDao()

    def update_or_create(self, defaults):
        registration = Registration(**defaults)
        self.dao.save(registration)
        return registration
