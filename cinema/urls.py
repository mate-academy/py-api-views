from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

halls_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create",
})
hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})


urlpatterns = [
    path("", include(router.urls)),
    path("cinema_halls/", halls_list, name="cinema_halls"),
    path("cinema_halls/<int:pk>/", hall_detail, name="cinema_hall_detail"),
    path("actors/", ActorList.as_view(), name="actors"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("genres/", GenreList.as_view(), name="genres"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),

]

app_name = "cinema"
