from django.contrib import admin

from .models import FavoriteRecipe


class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user__username', 'recipe__title')

admin.site.register(FavoriteRecipe, FavoriteRecipeAdmin)
