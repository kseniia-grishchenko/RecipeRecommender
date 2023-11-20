from django.urls import path
from . import views

urlpatterns = [
    path('favorites/', views.favorite_recipes, name='favorite_recipes'),
    path('add_to_favorites/<int:recipe_id>/', views.add_to_favorites, name='add_to_favorites'),
]
