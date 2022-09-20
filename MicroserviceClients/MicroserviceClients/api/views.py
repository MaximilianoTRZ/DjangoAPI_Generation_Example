from .models import City, Client
from .serializers import CitySerializer, ClientSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User

class index(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

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