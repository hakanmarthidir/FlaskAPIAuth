from flask import Blueprint
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Blueprint('api', __name__)


def create_app():
    from . import auth
    from . import sample
    app = FlaskAPI(__name__)
    app.config.from_object('config.DevelopmentConfig')
    app.config.from_pyfile('../config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(api, url_prefix='/api/v1')
    return app



