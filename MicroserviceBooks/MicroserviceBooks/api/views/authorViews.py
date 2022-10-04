from ..models.authorModel import Author
from ..serializers.authorSerializer import AuthorSerializer
from rest_framework import viewsets

class AuthorViewSet(viewsets.ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer