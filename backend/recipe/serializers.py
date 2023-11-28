from rest_framework import serializers
from .models import Recipe
from ingredient.serializers import IngredientNameSerializer, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientNameSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCreateSerializer(serializers.ModelSerializer):
    ingredients = IngredientNameSerializer(many=True)

    class Meta:
        model = Recipe
        exclude = ('author', )

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)

        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(**ingredient_data)
            recipe.ingredients.add(ingredient)

        return recipe
