import jwt
import datetime
from flask import current_app as app
from .managers import UserManager
from werkzeug.security import check_password_hash

class AuthController:

    @staticmethod
    def auth(username, password):
        """
        Return list of pokemon json objects given a filters dict
        :param filters: dict, fitlers from request
        :return List of dicts
        """
        user = UserManager.get({"name": username})
        
        if user and check_password_hash(user.password, password):
            token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, 'Th1s1ss3cr3t')
            return token.decode('UTF-8')
