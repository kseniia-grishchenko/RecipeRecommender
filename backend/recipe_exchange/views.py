from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import RecipeExchange, Recipe
from django.contrib.auth.models import User


def recipe_exchange(request):
    user_profile = User.objects.get(user=request.user)
    received_exchanges = RecipeExchange.objects.filter(receiver=user_profile)
    sent_exchanges = RecipeExchange.objects.filter(sender=user_profile)
    return render(request, 'recipe_exchange.html', {'received_exchanges': received_exchanges, 'sent_exchanges': sent_exchanges})
