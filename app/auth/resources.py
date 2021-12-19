from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request
from .controllers import AuthController


class AuthApi(Resource):
    def get(self):
        params = self.__get_parameters()

        if not params or not params["username"] or not params["password"]:
            return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        token = AuthController.auth(**params)

        if token:
            return jsonify({'token' : token})

        return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})
    
    def __get_parameters(self):
        """
        Get request parameters
        :param parameters: dict, values from request
        :return Dict
        """
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)

        return parser.parse_args()
