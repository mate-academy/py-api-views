from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallViewSet,
    GenreDetail,
    GenreList,
    MovieViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genres_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
]
