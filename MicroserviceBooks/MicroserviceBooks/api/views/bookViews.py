from ..models.bookModel import Book
from ..serializers.bookSerializer import BookSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
