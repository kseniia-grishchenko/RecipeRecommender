from django.shortcuts import render, get_object_or_404, redirect
from .models import RecipeRating, Recipe
from django.contrib.auth.models import User


def add_rating(request, recipe_id):
    user_profile = User.objects.get(user=request.user)
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        RecipeRating.objects.create(user_profile=user_profile, recipe=recipe, rating=rating, comment=comment)

    return redirect('recipe_detail.html', recipe_id=recipe_id)
