from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    GenreViewSet,
)

router = DefaultRouter()

router.register("actors", ActorViewSet)
router.register("movie", MovieViewSet)
router.register("cinema_hall", CinemaHallViewSet)
router.register("genre", GenreViewSet)

urlpatterns = router.urls

app_name = "cinema"
