from app.main import db


class BaseDao:

    def get_by_id(self, object_id):
        return self.model.query.get(object_id)

    def get_by_attributes(self, attributes):
        return self.model.query.filter_by(**attributes).first()

    def save(self, _object):
        db.session.add(_object)
        db.session.commit()

    def delete(self, _object):
        db.session.delete(_object)
        db.session.commit()
