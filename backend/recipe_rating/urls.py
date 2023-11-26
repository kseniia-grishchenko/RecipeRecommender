from django.urls import path
from .views import RecipeRatingListCreateView, RecipeRatingRetrieveUpdateDestroyView


urlpatterns = [
    path('', RecipeRatingListCreateView.as_view(), name='recipe-rating-list-create'),
    path('<int:pk>/', RecipeRatingRetrieveUpdateDestroyView.as_view(), name='recipe-rating-retrieve-update-destroy'),
]
