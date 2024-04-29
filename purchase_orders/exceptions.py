from werkzeug.exceptions import HTTPException

class QuantityExeption(HTTPException):
  code = 400