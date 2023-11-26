from django.contrib import admin

from .models import RecipeExchange


class RecipeExchangeAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'recipe')
    list_filter = ('sender', 'receiver', 'recipe')
    search_fields = ('sender__username', 'receiver__username', 'recipe__title')

admin.site.register(RecipeExchange, RecipeExchangeAdmin)
