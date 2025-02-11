from django.urls import path
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    GenreList,
    ActorList,
    CinemaHallViewSet,
    GenreDetail,
    ActorDetail
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")

app_name = "cinema"
urlpatterns = router.urls + [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
]
