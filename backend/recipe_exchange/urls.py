from django.shortcuts import render

from django.urls import path
from .views import recipe_exchange


urlpatterns = [
    path('recipe_exchange/', recipe_exchange, name='recipe_exchange'),
]
