from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateView,
    GenreDetailView,
    ActorListCreateView,
    ActorDetailView,
    CinemaHallViewSet,
    MovieViewSet
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreListCreateView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorListCreateView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("", include(router.urls)),
]
