from app.models import Registration
from app.main import db


class RegistrationDAO:
    def get_by_id(self, registration_id):
        return Registration.query.get(registration_id)

    def save(self, registration):
        db.session.add(registration)
        db.session.commit()

    def delete(self, registration):
        db.session.delete(registration)
        db.session.commit()
