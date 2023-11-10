from User_profile.models import UserProfile
from Recipes.models import Recipe
from django.db import models

class FavoriteRecipe(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # Додайте інші поля за необхідності

