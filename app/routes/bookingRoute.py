from flask import request
from app.services.bookingService import create_booking , get_bookings_by_email

def init_booking_routes(app):
    @app.route('/book', methods=['POST'])
    def book_class():
        data = request.get_json()
        return create_booking(data)
    
    @app.route('/bookings', methods=['GET'])
    def get_bookings():
        email = request.args.get('email')
        return get_bookings_by_email(email)