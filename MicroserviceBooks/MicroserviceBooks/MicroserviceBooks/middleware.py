"""
File in which we have the middleware for Django for Authenticating API requests
"""
import json
import jwt
import logging
import environ
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import asyncio
from time import sleep

# Initialize logger
logger = logging.getLogger(__name__)

# Get JWT secret key
env = environ.Env()
env.read_env()
SECRET_KEY = env("JWT_SECRET_KEY")


def create_response(request_id, code, message):

    """
    Function to create a response to be sent back via the API
    :param request_id:Id fo the request
    :param code:Error Code to be used
    :param message:Message to be sent via the APi
    :return:Dict with the above given params
    """

    try:
        req = str(request_id)
        data = {"data": message, "code": int(code), "request_id": req}
        return data
    except Exception as creation_error:
        logger.error(f'create_response:{creation_error}')


class isAuth(MiddlewareMixin):

    # """
    # Custom Middleware Class to process a request before it reached the endpoint
    # """
    # def __init__(self, get_response):
    #     self.get_response = get_response
    #     # One-time configuration and initialization.

    def __call__(self, request, **args):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print(request.headers.get('Authorization'))
        # print(request.headers)
        jwt_token = request.headers.get('Authorization')
        # logger.info(f"request received for endpoint {str(request.path)}")
        # print(jwt_token)
        # print('flag 1')
        # If token Exists
        # if jwt_token != None:
        try:
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
            # sleep(5)
            # userid = payload['user_id']
            # company_id = payload['company_id'] if 'company_id' in payload else None
            # print('flag 2')
            # print(payload)
            # return None
            response = self.get_response(request)
            return response
        except (jwt.ExpiredSignatureError):
            response = create_response("", 4001, {"message": "Authentication token has expired"})
            logger.info(f"Response {response}")
            return HttpResponse(json.dumps(response), status=401)
        except (jwt.DecodeError, jwt.InvalidTokenError):
            response = create_response("", 4001, {"message": "Authorization has failed, Please send valid token."})
            logger.info(f"Response {response}")
            return HttpResponse(json.dumps(response), status=401)


        response = self.get_response(request)
        return response


    # def process_request(self, request):

    #     """
    #     Custom middleware handler to check authentication for a user with JWT authentication
    #     :param request: Request header containing authorization tokens
    #     :type request: Django Request Object
    #     :return: HTTP Response if authorization fails, else None
    #     """
    #     print(request.headers)
    #     jwt_token = request.headers.get('Authorization')
    #     # logger.info(f"request received for endpoint {str(request.path)}")
    #     print(jwt_token)
    #     print('flag 1')
    #     # If token Exists
    #     # if jwt_token != None:
    #     try:
    #         payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    #         # sleep(5)
    #         # userid = payload['user_id']
    #         # company_id = payload['company_id'] if 'company_id' in payload else None
    #         print('flag 2')
    #         print(payload)
    #         return None
    #     except (jwt.ExpiredSignatureError):
    #         response = create_response("", 4001, {"message": "Authentication token has expired"})
    #         logger.info(f"Response {response}")
    #         return HttpResponse(json.dumps(response), status=401)
    #     except (jwt.DecodeError, jwt.InvalidTokenError):
    #         response = create_response("", 4001, {"message": "Authorization has failed, Please send valid token."})
    #         logger.info(f"Response {response}")
    #         return HttpResponse(json.dumps(response), status=401)
    #     # elif jwt_token == None:
    #     #     response = create_response(
    #     #         "", 4001, {"message": "Authorization not found, Please send valid token in headers"}
    #     #     )
    #     #     logger.info(f"Response {response}")
    #     #     return HttpResponse(json.dumps(response), status=401)
