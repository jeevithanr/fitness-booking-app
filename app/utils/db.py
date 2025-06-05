from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from app.models.classesModel import FitnessClass
from app.models.bookingModels import Booking

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)
