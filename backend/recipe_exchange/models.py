from django.contrib.auth.models import User
from recipe.models import Recipe
from django.db import models


class RecipeExchange(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.sender.username} to {self.receiver.username}: {self.recipe.title}"
