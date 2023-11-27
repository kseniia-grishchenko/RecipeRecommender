from django.db.models import Count
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Recipe
from .models import RecipeUserView
from .serializers import RecipeSerializer


class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RecipeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        if self.request.user:
            recipe = self.get_object()
            RecipeUserView.objects.create(recipe=recipe, user=self.request.user)
            return super().get(request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recipe_views_count(request):
    recipe_views_counter = RecipeUserView.objects.values('recipe').annotate(views_count=Count('recipe'))
    sorted_recipe_views_count = sorted(recipe_views_counter, key=lambda x: x['views_count'], reverse=True)

    result = []
    for entry in sorted_recipe_views_count:
        recipe_id = entry['recipe']
        views_count = entry['views_count']
        recipe = Recipe.objects.get(pk=recipe_id)

        recipe_data = RecipeSerializer(recipe).data
        result.append({'recipe': recipe_data, 'views_count': views_count})

    return Response(result)
