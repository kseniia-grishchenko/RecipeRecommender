from django.contrib.auth.models import User
from recipe.models import Recipe
from django.db import models


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.recipe.title}"
