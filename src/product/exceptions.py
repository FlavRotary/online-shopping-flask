from werkzeug.exceptions import HTTPException


class UnauthorizedException(HTTPException):
    pass

class ProductAlreadyInDatabase(HTTPException):
    pass

class ProductMissingFormDatabase(HTTPException):
    pass