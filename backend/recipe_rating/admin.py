from django.contrib import admin

from .models import RecipeRating


class RecipeRatingAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'recipe', 'rating')
    list_filter = ('user_profile', 'recipe', 'rating')
    search_fields = ('user_profile__username', 'recipe__title', 'rating')

admin.site.register(RecipeRating, RecipeRatingAdmin)
