from app.database import db
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import synonym
from app.utils.current_timestamp import current_timestamp

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    created_at = db.Column('created_at',
                           db.Integer,
                           default=current_timestamp,
                           nullable=False)
    updated_at = db.Column('updated_at',
                           db.Integer,
                           default=current_timestamp,
                           nullable=True,
                           onupdate=current_timestamp)
    
    posts = db.relationship('PostModel', back_populates="user",
                            lazy='joined')
    
    def _get_password(self):
        return self._password

    def _set_password(self, password):
        if password:
            password = password.strip()
        self._password = pbkdf2_sha256.hash(password)

    password_descriptor = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password_descriptor)

    def check_password(self, password):
        password = password.strip()
        if not password:
            return False
        return pbkdf2_sha256.verify(password, self.password)
        

    def __repr__(self):
        return "<Answer 'id:{}, email:{}'>".format(self.id, self.email)