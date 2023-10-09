from django.urls import path

from cinema.views import (MovieViewSet,
                          CinemaHallViewSet,
                          GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

cinemahall_list = CinemaHallViewSet.as_view(actions={
    "get": "list", "post": "create"})

cinemahall_detail = CinemaHallViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"})

urlpatterns = [
    # Genre url
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    # Actor url
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    # CinemaHall Url
    path("cinema_halls/", cinemahall_list, name="cinema-halls-list"),
    path("cinema_halls/<int:pk>/",
         cinemahall_detail,
         name="cinema-halls-detail")
    # Movie url


] + router.urls

app_name = "cinema"
