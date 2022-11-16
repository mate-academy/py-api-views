from django.urls import path

from cinema.views import movie_list, movie_detail, GenreList, GenreDetail, ActorList, ActorDetail, CinemaHallViewSet

cinema_hall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})
cinema_hall_detail = CinemaHallViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path(
        "movies/",
        movie_list,
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        movie_detail,
        name="movie-detail"
    ),
    path(
        "genres/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "actors/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    )
]

app_name = "cinema"
