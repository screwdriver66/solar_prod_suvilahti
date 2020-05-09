#could add some error handlers here, for example when there is no data in the forecast
# or whatever
class BaseError(Exception):
    """Base package error"""

class InvalidModelInputError(BaseError):
    """Error in the model input"""
