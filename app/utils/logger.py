import logging

logger = logging.getLogger("fitness_app")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")

file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)
