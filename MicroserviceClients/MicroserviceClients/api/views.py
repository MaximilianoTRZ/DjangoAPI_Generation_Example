from .models import City, Client
from .serializers import CitySerializer, ClientSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class index(APIView):

    def get(self, request, format=None):
      data = {
      'message':'index'
      }
      return Response(data,status=status.HTTP_200_OK)

class health(APIView):

    def get(self, request, format=None):
      data = {
      'status':'ok'
      }
      return Response(data,status=status.HTTP_200_OK)


"""
This viewset automatically provides `list`, `create`, `retrieve`,
`update` and `destroy` actions.

https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers

"""

"""
Al heredar de “ModelViewSet” ofrece los siguientes métodos:

GET /api/entity/city/
GET /api/entity/city/{pk}/
POST /api/entity/city/
PUT /api/entity/city/{pk}/
DELETE /api/entity/city/{pk}/
PATCH /api/entity/city/{pk}/

Además le indicamos que para la representación del recurso City debe de usar la clase “CitySerializer”.

"""

class CityViewSet(viewsets.ModelViewSet):
  queryset = City.objects.all()
  serializer_class = CitySerializer

class ClientViewSet(viewsets.ModelViewSet):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer

  def retrieve(self, request, pk=None, *args, **kwargs):

    client = Client.objects.get(pk=pk)
    bookParam = client.rentedBook
    res = requests.get('http://127.0.0.1:8000/api/entity/bookInstance/'+ bookParam)
    obtainedBook = res.json()
    print(obtainedBook)
    client.rentedBook = obtainedBook['id']
    serializer = ClientSerializer(client)

    return Response(serializer.data,status=status.HTTP_200_OK)

