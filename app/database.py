from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    # Todo: build decorator which turns 'in_transaction' to True then commit
    db.session.configure(info={'in_transaction': False})
    Migrate(app, db)