from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

cinema_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinema_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet)


urlpatterns = [
    path("genre/", GenreList.as_view(), name="genre_list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actor/", ActorList.as_view(), name="actor_list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("cinema-hall/", cinema_list, name="cinema_list"),
    path("cinema-hall/<int:pk>/", cinema_detail, name="cinema_detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
