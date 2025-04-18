from app.main import db


class Institution(db.Model):
    __tablename__ = 'institutions'
    __table_args__ = (db.UniqueConstraint('name', 'organization', 'category', name='unique_institution'),)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    acronym = db.Column(db.String(64))
    organization = db.Column(db.String(64))
    category = db.Column(db.String(64))

    def __repr__(self):
        return f'{self.name} - {self.id}'
