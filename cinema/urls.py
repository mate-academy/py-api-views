from django.urls import path
from rest_framework.routers import DefaultRouter
from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    ActorView,
    GenreView,
)

router = DefaultRouter()

router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema_halls"
)
router.register(
    "movies",
    MovieViewSet,
    basename="movies"
)

urlpatterns = [
    path("api/cinema/genre/", GenreView.as_view()),
    path("api/cinema/genre/<int:pk>/", GenreView.as_view()),
    path("api/cinema/actor/", ActorView.as_view()),
    path("api/cinema/actor/<int:pk>/", ActorView.as_view()),
] + router.urls

app_name = "cinema"
