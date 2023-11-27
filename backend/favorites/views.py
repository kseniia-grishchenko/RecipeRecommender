from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FavoriteRecipe
from .serializers import FavoriteRecipeSerializer, FavoriteRecipesSerializer
from recipe.models import Recipe


class FavoriteRecipeListCreateView(generics.ListCreateAPIView):
    queryset = FavoriteRecipe.objects.all()
    serializer_class = FavoriteRecipeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteRecipe.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        existing_favorite = FavoriteRecipe.objects.filter(user=self.request.user, recipe_id=request.data.get('recipe'))
        if existing_favorite.exists():
            existing_favorite.delete()
            return Response({'message': 'Рецепт видалено зі списку улюблених'}, status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FavoriteRecipeListView(generics.ListAPIView):
    queryset = FavoriteRecipe.objects.all()
    serializer_class = FavoriteRecipesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteRecipe.objects.filter(user=self.request.user)


class IsFavoriteRecipeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        user = request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        is_favorite = FavoriteRecipe.objects.filter(user=user, recipe=recipe).exists()
        return Response({"is_favorite": is_favorite})
