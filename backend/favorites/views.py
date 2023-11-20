from django.shortcuts import render, get_object_or_404, redirect
from .models import FavoriteRecipe, Recipe
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def favorite_recipes(request):
    user_profile = User.objects.get(user=request.user)
    favorites = FavoriteRecipe.objects.filter(user=user_profile)
    # TODO make an API views
    return render(request, 'favorite_recipes.html', {'favorites': favorites})


@login_required
def add_to_favorites(request, recipe_id):
    user_profile = User.objects.get(user=request.user)
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if not FavoriteRecipe.objects.filter(user_profile=user_profile, recipe=recipe).exists():
        FavoriteRecipe.objects.create(user_profile=user_profile, recipe=recipe)

# Todo what is this???
    return redirect('recipe_detail', recipe_id=recipe_id)
