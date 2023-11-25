from django.urls import path
from .views import RecipeRatingListCreateView, RecipeRatingRetrieveUpdateDestroyView


urlpatterns = [
    path('recipe-ratings/', RecipeRatingListCreateView.as_view(), name='recipe-rating-list-create'),
    path('recipe-ratings/<int:pk>/', RecipeRatingRetrieveUpdateDestroyView.as_view(), name='recipe-rating-retrieve-update-destroy'),
]
