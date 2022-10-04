from rest_framework import serializers
from ..models.bookInstanceModel import BookInstance

class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'