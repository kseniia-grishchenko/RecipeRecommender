from django.urls import path
from .views import FavoriteRecipeListCreateView, FavoriteRecipeListView


urlpatterns = [
    path('', FavoriteRecipeListCreateView.as_view(), name='favorite-recipe-list-create'),
    path('list/', FavoriteRecipeListView.as_view(), name='favorite-recipe-list'),
]
