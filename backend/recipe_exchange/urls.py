from django.shortcuts import render

from django.urls import path
from . import views

urlpatterns = [
    path('recipe_exchange/', views.recipe_exchange, name='recipe_exchange'),

]

