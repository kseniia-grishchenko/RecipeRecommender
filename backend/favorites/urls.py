from django.urls import path
from .views import FavoriteRecipeListCreateView, FavoriteRecipeListView, IsFavoriteRecipeView


urlpatterns = [
    path('', FavoriteRecipeListCreateView.as_view(), name='favorite-recipe-list-create'),
    path('<int:pk>/is_favorite/', IsFavoriteRecipeView.as_view(), name='favorite-recipe'),
    path('list/', FavoriteRecipeListView.as_view(), name='favorite-recipe-list'),
]
