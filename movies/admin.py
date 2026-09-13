from django.contrib import admin
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'date', 'movie', 'user', 'reported']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
