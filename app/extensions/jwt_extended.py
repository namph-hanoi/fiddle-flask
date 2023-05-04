from injector import Module, provider, singleton
from flask import make_response, jsonify
from flask_jwt_extended import JWTManager

jwt = JWTManager()

# WIP https://github.com/scorelab/LabelLab
# @jwt.token_in_blacklist_loader
# def token_is_blacklist(decypted_token):
#     jti = decypted_token["jti"]
#     return RevokedToken.is_jti_blacklisted(jti)


# The following methods are used for customizing jwt response/error messages.
@jwt.expired_token_loader
def expired_token_callback():
    response = {"message": "The token has expired.",
                "error": "token_expired"}
    return make_response(jsonify(response)), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    # We have to keep the argument here, since it's passed in by the jwt caller internally.
    response = {
        "message": "Signature verification failed.",
        "error": "invalid_token",
    }
    return make_response(jsonify(response)), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    response = {
        "message": "Request does not contain an access token.",
        "error": "authorization_required",
    }
    return make_response(jsonify(response)), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    response = {
        "message": "The token is not fresh.",
        "error": "fresh_token_required",
    }
    return make_response(jsonify(response)), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    response = {
        "message": "The token has been revoked.",
        "error": "token_revoked",
    }
    return make_response(jsonify(response)), 401