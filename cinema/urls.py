from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail
)


router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movie")

cinemahall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
cinemahall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})


urlpatterns = [
    path("", include(router.urls)),
    path("cinema_halls/", cinemahall_list, name="cinemahall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinemahall_detail,
        name="cinemahall-detail"
    ),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

]


app_name = "cinema"
