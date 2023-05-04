from flask.views import MethodView
from flask_smorest import Blueprint
from injector import Injector

injector = Injector()


blp = Blueprint("users", "users", url_prefix="/user", description="Operations on users")
# Todo: redis cache


@blp.route("/register")
class UserRegister(MethodView):
    def post(self): 
        return {"message": "User created successfully."}, 201
    


