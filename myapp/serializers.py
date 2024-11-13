from rest_framework import serializers
from .models import MyModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['name', 'description']
