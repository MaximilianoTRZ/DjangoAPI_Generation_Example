from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class login(viewsets.ViewSet):
    # get /api/v1/login/
    def list(self, request, format=None):
        return Response('NOT IMPLEMENTED',status=status.HTTP_200_OK)
    
    # get /api/v1/login/createExample/
    @action(methods=['get'], detail=False)
    def createExample(self, request):
        return Response('createExample',status=status.HTTP_200_OK)

    # post /api/v1/login/post
    @action(methods=['post'], detail=False)
    def post(self, request, pk=None):
        return Response('example post',status=status.HTTP_200_OK)

    # post /api/v1/login/1/example/
    @action(methods=['post'], detail=True)
    def example(self, request, pk=None):
        return Response('example detailed post',status=status.HTTP_200_OK)

