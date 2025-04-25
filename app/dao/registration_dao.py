from app.models import Registration
from app.dao.base_dao import BaseDao
from app.main import db


class RegistrationDao(BaseDao):
    def __init__(self):
        self.model = Registration

    def bulk_save_objects(self, registration_list):
        db.session.bulk_save_objects(registration_list)
        db.session.commit()