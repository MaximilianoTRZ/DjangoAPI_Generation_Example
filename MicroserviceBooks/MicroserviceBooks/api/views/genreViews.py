from ..models.genreModel import Genre
from ..serializers.genreSerializer import GenreSerializer
from rest_framework import viewsets

class GenreViewSet(viewsets.ModelViewSet):
  queryset = Genre.objects.all()
  serializer_class = GenreSerializer