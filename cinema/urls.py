from django.urls import path

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallViewSet,
    GenreDetail,
    GenreList,
)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    })
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    })

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>", ActorDetail.as_view()),
    path("cinema_halls/", cinema_hall_list, name="cinema-halls-list"),
    path(
        "cinema_halls/<int:pk>/",
        cinema_hall_detail,
        name="cinema-halls-list"
    )
]

app_name = "cinema"
