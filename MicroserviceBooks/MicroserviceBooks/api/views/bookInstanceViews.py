from ..models.bookInstanceModel import BookInstance
from ..serializers.bookInstanceSerializer import BookInstanceSerializer
from rest_framework import viewsets

class BookInstanceViewSet(viewsets.ModelViewSet):
  queryset = BookInstance.objects.all()
  serializer_class = BookInstanceSerializer
