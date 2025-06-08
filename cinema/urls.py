from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    movie_list, movie_detail,
    GenreList, GenreDetail,
    ActorListCreate, ActorRetrieveUpdateDestroy,
    CinemaHallViewSet, MovieViewSet,
)

router = DefaultRouter()
router.register(r"cinema-halls", CinemaHallViewSet)
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorListCreate.as_view(), name="actor-list-create"),
    path("actors/<int:pk>/", ActorRetrieveUpdateDestroy.as_view(),
         name="actor-retrieve-update-destroy"),
    path("", include(router.urls)),
]

app_name = "cinema"
