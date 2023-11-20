from django.urls import path
from .views import add_rating


urlpatterns = [
    path('<int:recipe_id>/', add_rating, name='add_rating'),
]
