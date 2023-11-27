from rest_framework import generics, permissions
from .models import RecipeExchange
from .serializers import RecipeExchangeSerializer


class RecipeExchangeListCreateView(generics.ListCreateAPIView):
    queryset = RecipeExchange.objects.all()
    serializer_class = RecipeExchangeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class RecipeExchangeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeExchange.objects.all()
    serializer_class = RecipeExchangeSerializer
    permission_classes = [permissions.IsAuthenticated]
