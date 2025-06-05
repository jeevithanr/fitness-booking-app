from flask import Flask, request
from flask_cors import CORS
from config import Config
from app.utils.db import init_db
from app.utils.logger import logger
from app.routes.classesRoute import init_classes_routes
from app.routes.bookingRoute import init_booking_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    
    init_db(app)
    
    init_classes_routes(app)
    init_booking_routes(app)
    
    @app.before_request
    def log_request():
        logger.info(f"Incoming request: {request.method} {request.path}")
        logger.info(f"Request body: {request.get_json(silent=True)}")

    @app.after_request
    def log_response(response):
        logger.info(f"Response status: {response.status}")
        return response
    return app