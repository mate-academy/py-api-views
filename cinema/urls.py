from django.urls import path, include

from .views import (
    GenreListCreateAPIView, GenreDetailAPIView,
    ActorListCreateAPIView, ActorDetailAPIView,
    CinemaHallViewSet, MovieViewSet
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"cinema/cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register(r"cinema/movies", MovieViewSet, basename="movie")


urlpatterns = [

    path("cinema/genres/", GenreListCreateAPIView.as_view(), name="genre-list-create"),
    path("cinema/genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),

    path("cinema/actors/", ActorListCreateAPIView.as_view(), name="actor-list-create"),
    path("cinema/actors/<int:pk>/", ActorDetailAPIView.as_view(), name="actor-detail"),

    path("api/", include(router.urls)),
]

app_name = "cinema"
