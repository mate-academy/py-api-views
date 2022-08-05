from django.urls import path, include

from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallList,
    CinemaHallDetail
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("cinema_halls/", CinemaHallList.as_view(), name="cinema_halls_list"),
    path("cinema_halls/<pk>/", CinemaHallDetail.as_view(), name="cinema_halls_detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
