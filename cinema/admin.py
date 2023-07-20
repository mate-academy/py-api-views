from django.contrib import admin

from cinema.models import Movie, Genre, Actor, CinemaHall


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "duration")
    list_filter = ("genres", "actors")
    search_fields = ("title", "description")
    filter_horizontal = ("genres", "actors")


admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(CinemaHall)
