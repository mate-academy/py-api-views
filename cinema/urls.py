from django.urls import path
from django.urls import include
from rest_framework import routers

from cinema.views import (MovieViewSet,
                          GenreList,
                          GenreDetail,
                          CinemaHallViewSet,
                          ActorList,
                          ActorDetail)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)


cinemahall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)

cinemahall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("cinema_halls/", cinemahall_list, name="cinemahall_list"),
    path("cinema_halls/<int:pk>/",
         cinemahall_detail,
         name="cinemahall_detail"),
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail")
]

app_name = "cinema"
