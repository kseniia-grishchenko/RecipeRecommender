from django.urls import path
from .views import RecipeExchangeListCreateView, RecipeExchangeRetrieveUpdateDestroyView


urlpatterns = [
    path('recipe-exchanges/', RecipeExchangeListCreateView.as_view(), name='recipe-exchange-list-create'),
    path('recipe-exchanges/<int:pk>/', RecipeExchangeRetrieveUpdateDestroyView.as_view(), name='recipe-exchange-retrieve-update-destroy'),
]
