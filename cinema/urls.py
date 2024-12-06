from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (GenreAPIView,
                    ActorGenericAPIView,
                    CinemaHallViewSet,
                    MovieViewSet)

app_name = "cinema"

cinema_hall_router = DefaultRouter()
cinema_hall_router.register(r"cinema_halls", CinemaHallViewSet)

movie_router = DefaultRouter()
movie_router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list-create"),
    path("actors/", ActorGenericAPIView.as_view(), name="actor-list-create"),
    path("", include(cinema_hall_router.urls)),
    path("", include(movie_router.urls)),
]
