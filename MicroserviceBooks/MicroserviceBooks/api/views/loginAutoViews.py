from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class loginAuto(viewsets.ViewSet):    
    
    # get /api/v1/login/auto/
    def list(self, request, format=None, detail=True, pk=None):
        return Response('NOT IMPLEMENTED getAll asdasd',status=status.HTTP_200_OK)

    # get /api/v1/login/auto/1
    def retrieve(self, request, pk=None, detail=False):
        return Response('NOT IMPLEMENTED getOneById sadasdasd',status=status.HTTP_200_OK)