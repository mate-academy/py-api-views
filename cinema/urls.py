from django.urls import path
from rest_framework.routers import DefaultRouter
from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    ActorView,
    GenreView,
)

router = DefaultRouter()

router.register('cinema_halls', CinemaHallViewSet)
router.register('movies', MovieViewSet)

urlpatterns = [
    path("path/cinema/genre/", GenreView.as_view()),
    path("path/cinema/actor/", ActorView.as_view()),
] + router.urls

app_name = "cinema"
