from django.urls import path, include
from rest_framework import routers


from cinema.views import (
    MovieViewSet, CinemaHallViewSet,
    ActorList, ActorDetail,
    GenreList, GenreDetail
)

movie_router = routers.DefaultRouter()
movie_router.register(
    "movies",
    MovieViewSet,
    basename="movies"
)

cinema_hall_router = routers.DefaultRouter()
cinema_hall_router.register(
    "cinema_halls",
    CinemaHallViewSet,
    basename="cinema-halls"
)


urlpatterns = [
    path("", include(movie_router.urls)),
    path("", include(cinema_hall_router.urls)),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
]

app_name = "cinema"
