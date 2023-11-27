from django.urls import path
from .views import RecipeExchangeListCreateView, RecipeExchangeRetrieveUpdateDestroyView


urlpatterns = [
    path('', RecipeExchangeListCreateView.as_view(), name='recipe-exchange-list-create'),
    path('<int:pk>/', RecipeExchangeRetrieveUpdateDestroyView.as_view(), name='recipe-exchange-retrieve-update-destroy'),
]
