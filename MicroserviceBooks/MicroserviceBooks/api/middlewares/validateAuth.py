from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from MicroserviceBooks.settings import env
import logging
import json
import jwt

env.read_env()
logger = logging.getLogger(__name__)



def create_response(request_id, code, message):

    try:
        req = str(request_id)
        data = {"data": message, "code": int(code), "request_id": req}
        return data
    except Exception as creation_error:
        logger.error(f'create_response:{creation_error}')


class validateAuth(MiddlewareMixin):

    def __call__(self, request, **args):

        jwt_token = request.headers.get('Authorization')

        try:
            payload = jwt.decode(jwt_token, env("JWT_SECRET"), algorithms=['HS256'])
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
