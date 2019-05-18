from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from .config import FlaskConfig
from .models import db


def create_app(db, config=FlaskConfig):
    app = Flask(__name__)
    from .views import github_view
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(github_view)
    return app


app = create_app(db)
