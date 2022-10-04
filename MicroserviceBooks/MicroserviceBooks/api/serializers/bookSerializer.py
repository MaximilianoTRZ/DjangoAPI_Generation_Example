from rest_framework import serializers
from ..models.bookModel import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'