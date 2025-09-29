# cinema/admin.py
from django.contrib import admin
from django.db.models import Count

from cinema.models import Actor, Genre, CinemaHall, Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration", "actors_total", "genres_total")
    search_fields = ("title", "description")
    list_filter = ("genres",)
    filter_horizontal = ("actors", "genres")
    ordering = ("title",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(
            _actors=Count("actors", distinct=True),
            _genres=Count("genres", distinct=True),
        )

    @admin.display(ordering="_actors", description="Actors")
    def actors_total(self, obj) -> int:
        return obj._actors

    @admin.display(ordering="_genres", description="Genres")
    def genres_total(self, obj) -> int:
        return obj._genres
