from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector, request
from flask_sqlalchemy import SQLAlchemy
from ..database import init_db, db

# from app.extensions import cache
from app.config import Config

def create_app(config_mode='development'):
    app = Flask(Config.NAME)
    app.config.from_object(Config)
    app.secret_key = Config.APP_SECRET
    app.url_map.strict_slashes = False

    with app.app_context():
        init_db(app)

    # Todo: register cache extension
    # Todo: register_routes

    CORS(app,
         send_wildcard=True,
         expose_headers=['x-auth-token', "content-disposition"])
    # Todo: Error handler for all Blueprint
    FlaskInjector(app=app, modules=[configure])

    return app


def configure(binder):
    binder.bind(
        SQLAlchemy,
        to=db,
        scope=request,
    )