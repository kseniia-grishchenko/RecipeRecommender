from rest_framework import serializers
from .models import RecipeExchange


class RecipeExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeExchange
        fields = '__all__'
