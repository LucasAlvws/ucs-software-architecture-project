from app.main import db
from app.models import Registration

class RegistrationDao:
    def __init__(self):
        self.model = Registration

    def get_by_id(self, object_id):
        return self.model.query.get(object_id)

    def get_by_attributes(self, attributes):
        return self.model.query.filter_by(**attributes).first()

    def save(self, _object):
        db.session.add(_object)
        db.session.commit()

    def save_dataframe(self, dataframe):
        dataframe.to_sql('registrations', con=db.engine, if_exists='append', index=False)

    def delete(self, _object):
        db.session.delete(_object)
        db.session.commit()
