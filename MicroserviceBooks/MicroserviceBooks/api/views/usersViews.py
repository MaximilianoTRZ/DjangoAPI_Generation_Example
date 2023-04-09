from rest_framework import viewsets, status
from rest_framework.response import Response
from ..middlewares.validateAuth import validateAuth
from django.utils.decorators import method_decorator


# def get(request, username):
#     now = '20221029'
#     return Response('NOT IMPLEMENTED getAll',status=status.HTTP_200_OK)

class users(viewsets.ViewSet):

    @method_decorator(validateAuth)
    def list(self, request, username=None, format=None, detail=False):
        print('get list')
        print(request.query_params)
        return Response('NOT IMPLEMENTED getAll',status=status.HTTP_200_OK)
        
    @method_decorator(validateAuth)
    def retrieve(self, request, pk=None, detail=False):
        # print(request.headers)
        # print(request.body)
        # pk=parameter
        print('get retrieve')
        return Response('NOT IMPLEMENTED getOneById aaaa',status=status.HTTP_200_OK)