from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreAPIView,
    GenreDetailAPIView,
    ActorAPIView,
    ActorDetailAPIView,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("cinema/genres/", GenreAPIView.as_view()),
    path("cinema/genres/<int:pk>/", GenreDetailAPIView.as_view()),
    path("cinema/actors/", ActorAPIView.as_view()),
    path("cinema/actors/<int:pk>/", ActorDetailAPIView.as_view()),
    path("cinema/", include(router.urls)),
]
