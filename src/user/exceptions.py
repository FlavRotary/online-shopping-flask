from werkzeug.exceptions import HTTPException


class UnauthorizedException(HTTPException):
    pass


class EmailAlreadyRegistered(HTTPException):
    pass


class InvalidUserEmailException(HTTPException):
    pass
