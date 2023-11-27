from django.urls import path
from .views import RecipeListCreateView, RecipeRetrieveUpdateDestroyView, recipe_views_count


urlpatterns = [
    path('', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('<int:pk>/', RecipeRetrieveUpdateDestroyView.as_view(), name='recipe-retrieve-update-destroy'),
    path('popular-recipes/', recipe_views_count, name='popular-recipes'),
]
