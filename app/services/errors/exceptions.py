import logging
from http import HTTPStatus

logger = logging.getLogger(__name__)


class UnauthorizedError(Exception):
    def __init__(self, error, status_code=HTTPStatus.UNAUTHORIZED):
        """
        This function is used to raise an exception when the user is not authorized to access the resource
        
        :param error: The error message to be returned to the user
        :param status_code: The HTTP status code to return
        """
        Exception.__init__(self)
        self.error = error
        self.status_code = status_code


class ForbiddenError(Exception):
    def __init__(self, error='Recurso não encontrado',
                 status_code=HTTPStatus.FORBIDDEN):
        """
        It's a function that takes in an error message and a status code, and returns an error message and a
        status code
        
        :param error: The error message that will be returned to the user, defaults to Recurso não
        encontrado (optional)
        :param status_code: The HTTP status code to return
        """
                 
        Exception.__init__(self)
        self.error = error
        self.status_code = status_code


class NotFoundError(Exception):
    def __init__(self, error='Recurso não encontrado',
                 status_code=HTTPStatus.NOT_FOUND):
        """
        It's a function that takes in an error message and a status code, and returns an error message and a
        status code
        
        :param error: The error message that will be returned to the user, defaults to Recurso não
        encontrado (optional)
        :param status_code: The HTTP status code that will be returned to the client
        """
                 
        Exception.__init__(self)
        self.error = error
        self.status_code = status_code


class GenerateError(Exception):
    """Generate generic error"""

    def __init__(self, error, status_code=500, errors=[]):
        """
        This function is a constructor that takes in an error message, a status code, and a list of errors.
        It then sets the message, status code, and errors to the values passed in
        
        :param error: The error message
        :param status_code: The HTTP status code, defaults to 500 (optional)
        :param errors: A list of errors that are related to the error
        """
        self.message = error
        self.status_code = status_code
        self.errors = errors
        super().__init__(self.message, self.errors)
