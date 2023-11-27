from django.contrib.auth.models import User
from django.db import models

from ingredient.models import Ingredient


def recipe_directory_path(instance, filename):
    return f'recipes/{instance.title}.{filename.split(".")[-1]}'


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to=recipe_directory_path)

    def __str__(self) -> str:
        return self.title


class RecipeUserView(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True)
