from django.shortcuts import render, get_object_or_404, redirect
from .models import FavoriteRecipe, Recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def favorite_recipes(request):
    user_profile = UserProfile.objects.get(user=request.user)
    favorites = FavoriteRecipe.objects.filter(user_profile=user_profile)
    return render(request, 'favorite_recipes.html', {'favorites': favorites})

@login_required
def add_to_favorites(request, recipe_id):
    user_profile = UserProfile.objects.get(user=request.user)
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    # Check if recipe is not yet added to the list
    if not FavoriteRecipe.objects.filter(user_profile=user_profile, recipe=recipe).exists():
        FavoriteRecipe.objects.create(user_profile=user_profile, recipe=recipe)

    return redirect('recipe_detail', recipe_id=recipe_id)
