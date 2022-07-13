from django.contrib import admin

from cinema.models import Movie, Genre, Actor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre)

admin.site.register(Actor)
