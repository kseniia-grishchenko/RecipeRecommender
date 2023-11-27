from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import FavoriteRecipe
from .serializers import FavoriteRecipeSerializer


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
