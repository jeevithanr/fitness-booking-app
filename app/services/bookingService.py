import uuid
from flask import jsonify
from app.models.bookingModels import Booking, FitnessClass
from app.utils.db import db
from app.utils.logger import logger
from http import HTTPStatus

def create_booking(data):
    class_id = data.get('class_id')
    name = data.get('client_name')
    email = data.get('client_email')

    logger.info(f"Attempting booking: class_id={class_id}, name={name}, email={email}")

    if not all([class_id, name, email]):
        logger.warning("Booking failed due to missing fields.")
        return jsonify({'error': 'Missing required fields'}), HTTPStatus.BAD_REQUEST

    fitness_class = FitnessClass.query.get(class_id)
    if not fitness_class:
        logger.warning(f"Booking failed: class {class_id} not found.")
        return jsonify({'error': 'Class not found'}), HTTPStatus.NOT_FOUND

    if fitness_class.available_slots <= 0:
        logger.info(f"Booking rejected: class {class_id} is fully booked.")
        return jsonify({'error': 'No available slots'}), HTTPStatus.BAD_REQUEST

    booking_id = str(uuid.uuid4())

    booking = Booking(
        id=booking_id,
        class_id=class_id,
        client_name=name,
        client_email=email
    )

    try:
        db.session.add(booking)
        fitness_class.available_slots -= 1
        db.session.commit()
        logger.info(f"Booking successful: booking_id={booking_id}")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Booking failed due to DB error: {str(e)}")
        return jsonify({'error': 'Booking failed', 'details': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify({'message': 'Booking successful', 'booking_id': booking_id}), HTTPStatus.CREATED


def get_bookings_by_email(email):
    logger.info(f"Fetching bookings for email: {email}")
    
    if not email:
        logger.warning("Email missing in booking fetch request.")
        return jsonify({'error': 'Email is required'}), HTTPStatus.BAD_REQUEST

    bookings = Booking.query.filter_by(client_email=email).all()

    if not bookings:
        logger.info(f"No bookings found for email: {email}")
        return jsonify({'message': 'No bookings found for this email'}), HTTPStatus.NOT_FOUND

    booking_list = []
    for booking in bookings:
        booking_list.append({
            'id': booking.id,
            'class_id': booking.class_id,
            'client_name': booking.client_name,
            'client_email': booking.client_email
        })

    logger.info(f"Found {len(booking_list)} bookings for email: {email}")
    return jsonify({'bookings': booking_list}), HTTPStatus.OK

