from rest_framework import serializers
from ..models.authorModel import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'