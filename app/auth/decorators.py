import jwt
from flask import request, jsonify, current_app as app
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if app.config.get("TESTING"):
            return f(*args, **kwargs)

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'][7:]

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
        except:
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)

    return decorator
