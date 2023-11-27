from rest_framework import serializers
from .models import FavoriteRecipe
from recipe.serializers import RecipeSerializer


class FavoriteRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRecipe
        fields = ('recipe',)


class FavoriteRecipesSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(many=False)

    class Meta:
        model = FavoriteRecipe
        fields = ('recipe',)
