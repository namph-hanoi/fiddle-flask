from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector, request
from flask_sqlalchemy import SQLAlchemy
from ..database import init_db, db
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from app.resources.user import blp as UserBlueprint
from app.config import Config
from ..models import *
from ..extensions import (cache, jwt)

def create_app():
    app = Flask(Config.NAME)
    app.config.from_object(Config)
    app.secret_key = Config.APP_SECRET
    app.url_map.strict_slashes = False
    api = Api(app)

    with app.app_context():
        init_db(app)
        jwt.init_app(app)
        cache.init_app(app)


    CORS(app,
         send_wildcard=True,
         expose_headers=['x-auth-token', "content-disposition"])
    # Todo: Error handler for all Blueprint
    FlaskInjector(app=app, modules=[configure])

    api.register_blueprint(UserBlueprint)


    return app


def configure(binder):
    binder.bind(
        SQLAlchemy,
        to=db,
        scope=request,
    )