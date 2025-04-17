from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def create_app():
    from app.models import Course, Registration, Institution  # noqa: F401
    from app.controllers.data import upload_bp

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(upload_bp)

    return app
