import uuid
import pytz
from http import HTTPStatus
from app.models.classesModel import FitnessClass
from flask import jsonify
from app.utils.db import db
from app.utils.logger import logger
from datetime import datetime,timezone

def get_all_classes(user_timezone):
    try:
        logger.info(f"Fetching all classes for timezone: {user_timezone}")
        classes = FitnessClass.query.all()
        user_timezone = user_timezone.strip()
        target_tz = pytz.timezone(user_timezone)

        class_list = []
        for cls in classes:
            dt = cls.date_time
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            local_time = dt.astimezone(target_tz)
            class_data = {
                "id": cls.id,
                "name": cls.name,
                "instructor": cls.instructor,
                "datetime": local_time.strftime('%Y-%m-%d %H:%M:%S'),
                "available_slots": cls.available_slots
            }
            class_list.append(class_data)

    except Exception as e:
        logger.error(f"Error fetching classes: {str(e)}")
        return jsonify({
            "success": False,
            "message": str(e),
            "data": [],
            "count": 0,
            "status_code": HTTPStatus.INTERNAL_SERVER_ERROR
        }), HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        logger.info(f"Fetched {len(class_list)} classes.")
        return jsonify({
            "success": True,
            "message": "Classes fetched successfully",
            "data": class_list,
            "count": len(class_list),
            "status_code": HTTPStatus.OK
        }), HTTPStatus.OK



def createClasses(data):
    try:
        name = data.get('name')
        date_time_str = data.get('date_time')
        instructor = data.get('instructor')
        available_slots = data.get('available_slots')

        logger.info(f"Creating class: {name} at {date_time_str} with instructor {instructor} and {available_slots} slots.")

        if not all([name, date_time_str, instructor, available_slots]):
            logger.warning("Class creation failed due to missing fields.")
            raise ValueError("Missing required fields")

        ist = pytz.timezone('Asia/Kolkata')
        naive_dt = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        ist_dt = ist.localize(naive_dt)
        utc_dt = ist_dt.astimezone(pytz.utc)

        new_class = FitnessClass(
            id=str(uuid.uuid4()),
            name=name,
            date_time=utc_dt,
            instructor=instructor,
            available_slots=int(available_slots)
        )

        db.session.add(new_class)
        db.session.commit()

        logger.info(f"Class created successfully: {new_class.id}")

        return {
            "success": True,
            "message": "Fitness class created successfully",
            "data": {
                "id": new_class.id,
                "name": new_class.name,
                "instructor": new_class.instructor,
                "available_slots": new_class.available_slots,
                "date_time": new_class.date_time.strftime('%Y-%m-%d %H:%M:%S')
            },
            "status_code": HTTPStatus.CREATED
        }, HTTPStatus.CREATED

    except Exception as e:
        logger.error(f"Error while creating class: {str(e)}")
        return {
            "success": False,
            "message": str(e),
            "data": [],
            "status_code": HTTPStatus.INTERNAL_SERVER_ERROR
        }, HTTPStatus.INTERNAL_SERVER_ERROR
