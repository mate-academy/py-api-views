from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreAPIView,
    ActorGenericAPIView,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register(r"cinemahalls", CinemaHallViewSet)
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("actors/", ActorGenericAPIView.as_view(), name="actor-list"),
    path("/", include(router.urls)),
]
