from flask.views import MethodView
from flask import abort
from flask_smorest import Blueprint
from injector import Injector
from app.database import db
from sqlalchemy import or_
from app.models import UserModel
from passlib.hash import pbkdf2_sha256
from app.schemas.user import UserRegisterSchema

injector = Injector()


blp = Blueprint("users", "users", url_prefix="/user", description="Operations on users")
# Todo: redis cache

#  Todo: inject model
@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        try:
            if UserModel.query.filter(
                or_(
                    UserModel.username == user_data["username"],
                    UserModel.email == user_data["email"],
                )
            ).first():
                abort(409, message="A user with that username or email already exists.")

            user = UserModel(
                username=user_data["username"],
                email=user_data["email"],
                # Todo: create a class function for hash inside User model
                password=pbkdf2_sha256.hash(user_data["password"]),
            )
            db.session.add(user)
            db.session.commit()
        except Exception as error:
            print("Error occured:", error)
            
        return {"message": "User created successfully."}, 201
    


