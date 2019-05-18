import os


class FlaskConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
