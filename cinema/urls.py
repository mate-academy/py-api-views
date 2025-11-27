from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    movie_list,
    movie_detail,
    genre_list,
    genre_detail,
    ActorList,
    ActorDetail,
    CinemaHallView,
    MovieViewSet,
)

cinema_hall_list = CinemaHallView.as_view(actions={"get": "list",
                                                   "post": "create"})
cinema_hall_detail = CinemaHallView.as_view(
    actions={"get": "retrieve", "put": "update", "delete": "destroy"}
)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahalls/", cinema_hall_list, name="cinemahall-list"),
    path("cinemahalls/<int:pk>/", cinema_hall_detail,
         name="cinemahall-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
