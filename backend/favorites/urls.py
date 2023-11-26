from django.urls import path
from .views import FavoriteRecipeListCreateView


urlpatterns = [
    path('', FavoriteRecipeListCreateView.as_view(), name='favorite-recipe-list-create'),
]
