from django.urls import path
from rest_framework.routers import DefaultRouter
from cinema.views import (
    CinemaHallViewSet,
    MovieViewSet,
    ActorList,
    GenreList,
    ActorDetail,
    GenreDetail,
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
    path("api/cinema/genre/", GenreList.as_view()),
    path("api/cinema/genre/<int:pk>/", GenreDetail.as_view()),
    path("api/cinema/actor/", ActorList.as_view()),
    path("api/cinema/actor/<int:pk>/", ActorDetail.as_view()),
] + router.urls

app_name = "cinema"
