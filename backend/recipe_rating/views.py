from rest_framework import generics, permissions
from .models import RecipeRating
from .serializers import RecipeRatingSerializer


class RecipeRatingListCreateView(generics.ListCreateAPIView):
    queryset = RecipeRating.objects.all()
    serializer_class = RecipeRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


class RecipeRatingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeRating.objects.all()
    serializer_class = RecipeRatingSerializer
    permission_classes = [permissions.IsAuthenticated]
