from django.urls import path
from .views import IngredientListCreateView, IngredientRetrieveUpdateDestroyView


urlpatterns = [
    path('ingredients/', IngredientListCreateView.as_view(), name='ingredient-list-create'),
    path('ingredients/<int:pk>/', IngredientRetrieveUpdateDestroyView.as_view(), name='ingredient-retrieve-update-destroy'),
]
