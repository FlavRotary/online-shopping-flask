from functools import wraps

import jwt
from flask import request, current_app, g

from exceptions import UnauthorizedException


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization', None)

        if token is None:
            raise UnauthorizedException
        try:
            decoded = jwt.decode(token.replace('Bearer ', ''), current_app.config['JWT_SECRET'], algorithms=['HS256'])
        except jwt.DecodeError:
            raise UnauthorizedException

        g.logged_in_user = decoded['sub']
        return func(*args, **kwargs)

    return wrapper
