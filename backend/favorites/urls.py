from django.urls import path
from .views import favorite_recipes, add_to_favorites


urlpatterns = [
    path('favorites/', favorite_recipes, name='favorite_recipes'),
    path('add_to_favorites/<int:recipe_id>/', add_to_favorites, name='add_to_favorites'),
]
