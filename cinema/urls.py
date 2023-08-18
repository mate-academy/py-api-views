from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreList,
                          GenreDetail,
                          ActorList,
                          CinemaHallViewSet, ActorDetail, MovieViewSet,
                          )

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinema_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})
cinema_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})
urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", cinema_list, name="cinema-list"),
    path("cinema_halls/<int:pk>/", cinema_detail, name="cinema-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
