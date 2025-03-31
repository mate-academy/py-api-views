from django.urls import path, include
# from rest_framework import routers
#
# from cinema.views import (
#     GenreList,
#     GenreDetail,
#     ActorList,
#     ActorDetail,
#     MovieViewSet,
#     CinemaHallViewSet
# )
#
# cinema_hall_list = CinemaHallViewSet.as_view(
#     actions={
#         "get": "list",
#         "post": "create"
#     }
# )
#
# cinema_hall_detail = CinemaHallViewSet.as_view(
#     actions={
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "destroy"
#     }
# )
#
# router = routers.DefaultRouter()
#
# router.register("movies", MovieViewSet, basename="movies")
#
#
# urlpatterns = [
#     path("genre/", GenreList.as_view(), name="genre_list"),
#     path("genre/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
#
#     path("actor/", ActorList.as_view(), name="actor_list"),
#     path("actor/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
#
#     path("cinemahall/", cinema_hall_list, name="cinema_hall_list"),
#     path(
#         "cinemahall/<int:pk>/",
#         cinema_hall_detail,
#         name="cinema_hall_detail"
#     ),
#
#     path("", include(router.urls)),
#
# ]
#
# app_name = "cinema"

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

movie_list = MovieViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

movie_detail = MovieViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallViewSet.as_view(
        actions={
            "get": "list",
            "post": "create",
        }
    ), name="cinema-hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view(
        actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy"
        }
    ), name="cinema-hall-detail"),
]

app_name = "cinema"
