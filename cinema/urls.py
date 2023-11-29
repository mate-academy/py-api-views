from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet,
                          MovieViewSet)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinamehall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
cinamehall_detail = CinemaHallViewSet.as_view(
    actions={"get": "retrieve",
             "put": "update",
             "path": "partial_update",
             "delete": "destroy"}
)

urlpatterns = [
    path("movies/", include(router.urls)),
    path("genres/",
         GenreList.as_view(),
         name="genre-list"),
    path("genres/<int:pk>/",
         GenreDetail.as_view(),
         name="genre-detail"),
    path("actors/",
         ActorList.as_view(),
         name="actor-list"),
    path("actors/<int:pk>/",
         ActorDetail.as_view(),
         name="actor-detail"),
    path("cinemahall/",
         cinamehall_list,
         name="cinemahall-list"),
    path("cinemahall/<int:pk>/",
         cinamehall_detail,
         name="cinemahall-detail"),
]

app_name = "cinema"
