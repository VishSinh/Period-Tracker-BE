from rest_framework.exceptions import APIException
from rest_framework import status


class CustomException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'An error occured'


class BadRequest(Exception):
    status_code = status.HTTP_400_BAD_REQUEST
    message = 'The request is invalid or malformed'
    
    
class Unauthorized(Exception):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = 'You are not authorized to access this resource'
    
    
class TooManyRequests(Exception):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    message = 'You have exceeded the rate limit'
    

class NotFound(Exception):
    status_code = status.HTTP_404_NOT_FOUND
    message = 'The requested resource was not found'
    

class Conflict(Exception):
    status_code = status.HTTP_409_CONFLICT
    message = 'The request conflicts with the current state of the resource'