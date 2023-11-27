from rest_framework import serializers
from .models import Recipe
from ingredient.serializers import IngredientNameSerializer


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientNameSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'
