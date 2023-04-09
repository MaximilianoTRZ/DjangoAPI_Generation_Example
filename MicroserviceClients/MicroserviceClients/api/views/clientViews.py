from ..models.clientModel import Client
from ..serializers.clientSerializer import ClientSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from MicroserviceClients.settings import env
from requests.api import get



class ClientViewSet(viewsets.ModelViewSet):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer

  def retrieve(self, request, pk=None, *args, **kwargs):

    client = Client.objects.get(pk=pk)
    bookParam = client.rentedBook
    res = get(env("BOOKS_MICROSERVICE_URL")+'/api/entity/bookInstance/'+bookParam)
    obtainedBook = res.json()
    print(obtainedBook)
    client.rentedBook = obtainedBook['id']
    serializer = ClientSerializer(client)

    return Response(serializer.data,status=status.HTTP_200_OK)