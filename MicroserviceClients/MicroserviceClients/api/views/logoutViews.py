from rest_framework import viewsets, status
from rest_framework.response import Response

class logout(viewsets.ViewSet):

    # get /api/v1/logout/
    def list(self, request, format=None):
        return Response('NOT IMPLEMENTED',status=status.HTTP_200_OK)
    
    # get /api/v1/logout/{pk}
    def retrieve(self, request, format=None, pk=None):
        return Response('NOT IMPLEMENTED',status=status.HTTP_200_OK)