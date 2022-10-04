from ..models.addressModel import Address
from ..serializers.addressSerializer import AddressSerializer
from rest_framework import viewsets

class AddressViewSet(viewsets.ModelViewSet):
  queryset = Address.objects.all()
  serializer_class = AddressSerializer