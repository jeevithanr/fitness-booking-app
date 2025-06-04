from app.utils.db import db
from app.models.classesModel import FitnessClass

class Booking(db.Model):
    __tablename__ = 'Bookings'
     
    id = db.Column(db.String(36), primary_key=True)
    class_id = db.Column(db.String(36), db.ForeignKey('fitness_class.id'), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    client_email = db.Column(db.String(100), nullable=False)