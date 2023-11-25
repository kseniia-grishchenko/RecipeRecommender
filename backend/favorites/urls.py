from django.urls import path
from .views import FavoriteRecipeListCreateView, UserFavoriteRecipeListView


urlpatterns = [
    path('favorite-recipes/', FavoriteRecipeListCreateView.as_view(), name='favorite-recipe-list-create'),
    path('user-favorite-recipes/<int:user_id>/', UserFavoriteRecipeListView.as_view(), name='user-favorite-recipe-list'),
]
