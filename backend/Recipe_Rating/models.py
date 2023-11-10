from User_profile.models import UserProfile
from Recipes.models import Recipe
from django.db import models

class RecipeRating(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    # Додайте інші поля за необхідності
