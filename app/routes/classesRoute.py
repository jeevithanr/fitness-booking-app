from flask import request
from app.services.classesService import get_all_classes, createClasses

def init_classes_routes(app):
    @app.route('/classes', methods=['GET'])
    def get_classes():
        user_timezone = request.args.get('timezone', default='Asia/Kolkata')
        return get_all_classes(user_timezone=user_timezone)
        
    @app.route('/classes/create', methods=['POST'])
    def create_classes():
        data = request.json
        return createClasses(data)