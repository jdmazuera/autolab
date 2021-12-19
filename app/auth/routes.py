from flask_restful import Api
from flask import current_app as app
from .resources import AuthApi

api = Api(app)

api.add_resource(
    AuthApi,
    "/auth",
    endpoint="auth"
)