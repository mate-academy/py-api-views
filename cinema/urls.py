from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
    MovieViewSet
)

cinemahall_list = CinemaHallViewSet.as_view(actions={
    "get": "list",
    "post": "create"
}
)
cinemahall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
}
)

movie_router = routers.DefaultRouter()
movie_router.register("movies", MovieViewSet)

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("cinema_halls/", cinemahall_list, name="cinema-hall-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinemahall_detail,
        name="cinema-hall-detail"),
    path("", include(movie_router.urls)),
]

app_name = "cinema"
