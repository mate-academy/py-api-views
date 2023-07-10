from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet, MovieViewSet,
)
# cinema_hall_list = CinemaHallViewSet.as_view(
#     actions={
#         "get": "list",
#         "post": "create"
#     })
# cinema_hall_detail = CinemaHallViewSet.as_view(
#     actions={
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "destroy"
#     })

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_hall", CinemaHallViewSet)

urlpatterns = [
    path("movie/", movie_list, name="movie-list"),
    path("movie/<int:pk>/", movie_detail, name="movie-detail"),
    path("genre/", GenreList.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    # path("cinema_hall/", cinema_hall_list, name="cinema-hall-list"),
    # path("cinema_hall/<int:pk>/", cinema_hall_detail,
    # name="cinema-hall-detail"),
    path("", include(router.urls))
]

app_name = "cinema"
