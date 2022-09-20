from .models import Author, Genre, Book, BookInstance
from .serializers import AuthorSerializer,GenreSerializer,BookSerializer,BookInstanceSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
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

class login(APIView):

    def get(self, request, format=None):
        data = {
        'message':'login',
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

GET /api/entity/author/
GET /api/entity/author/{pk}/
POST /api/entity/author/
PUT /api/entity/author/{pk}/
DELETE /api/entity/author/{pk}/
PATCH /api/entity/author/{pk}/

Además le indicamos que para la representación del recurso Author debe de usar la clase “AuthorSerializer”.

"""
class AuthorViewSet(viewsets.ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ModelViewSet):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookInstanceViewSet(viewsets.ModelViewSet):
  queryset = BookInstance.objects.all()
  serializer_class = BookInstanceSerializer

