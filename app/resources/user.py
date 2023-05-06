from flask.views import MethodView
from flask_smorest import abort
from flask_smorest import Blueprint
from injector import Injector
from app.database import db
from sqlalchemy import or_
from app.models import UserModel
from passlib.hash import pbkdf2_sha256
from app.schemas.user import (UserRegisterSchema, UserSchema)
from flask_jwt_extended import (create_refresh_token, create_access_token)

injector = Injector()


blp = Blueprint("users", "users", url_prefix="/api/v1/user", description="Operations on users")
# Todo: redis cache

#  Todo: inject model
@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
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
            password=user_data["password"],
        )
        db.session.add(user)
        # Todo: create decorator to auto commit or rollback
        db.session.commit()            
        return {"message": "User created successfully."}, 201
    

@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        print('user_data')
        user = UserModel.query.filter(
            UserModel.username == user_data["username"]
        ).first()

        if user and user.check_password(user_data["password"]):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}

        abort(401, message="Invalid credentials.")

