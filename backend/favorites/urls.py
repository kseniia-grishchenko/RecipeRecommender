from django.urls import path
from .views import FavoriteRecipeListCreateView


urlpatterns = [
    path('favorite-recipes/', FavoriteRecipeListCreateView.as_view(), name='favorite-recipe-list-create'),
]
