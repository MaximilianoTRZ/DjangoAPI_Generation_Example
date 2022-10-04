from ..models.cityModel import City
from ..serializers.citySerializer import CitySerializer
from rest_framework import viewsets

class CityViewSet(viewsets.ModelViewSet):
  queryset = City.objects.all()
  serializer_class = CitySerializer


