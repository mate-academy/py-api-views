from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateAPIView,
    GenreDetailAPIView,
    ActorListCreateAPIView,
    ActorDetailAPIView,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreListCreateAPIView.as_view()),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view()),
    path("actors/", ActorListCreateAPIView.as_view()),
    path("actors/<int:pk>/", ActorDetailAPIView.as_view()),
    path("", include(router.urls)),
]
