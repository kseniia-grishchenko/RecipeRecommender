from django.contrib.auth.models import User
from recipe.models import Recipe
from django.db import models


class RecipeRating(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self) -> str:
        return f"{self.user_profile.username} - {self.recipe.title} ({self.rating} stars)"
