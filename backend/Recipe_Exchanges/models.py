from User_profile.models import UserProfile
from Recipes.models import Recipe
from django.db import models

class RecipeExchange(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='receiver', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    message = models.TextField()
    # Додайте інші поля за необхідності

