from app.models import Institution
from app.main import db


class InstitutionDAO:
    def get_by_id(self, instituition_id):
        return Institution.query.get(instituition_id)

    def save(self, instituition):
        db.session.add(instituition)
        db.session.commit()

    def delete(self, instituition):
        db.session.delete(instituition)
        db.session.commit()
