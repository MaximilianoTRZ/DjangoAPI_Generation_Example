from .models import Author, Genre, Book, BookInstance
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        #fields = '__all__'
        fields = ['name','lastName','birthDay']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author','summary','genre']

class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ['book','status','return_date']
