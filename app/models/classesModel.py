from app.utils.db import db

class FitnessClass(db.Model):
    __tablename__ = 'fitness_class'
       
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    available_slots = db.Column(db.Integer, nullable=False)