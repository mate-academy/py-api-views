from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallViewSet,
    GenreDetail,
    GenreList,
    MovieViewSet,
    movie_detail,
    movie_list,
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"cinema-halls", CinemaHallViewSet, basename="cinema-hall")

urlpatterns = [
    path("movies-func/", movie_list, name="movie-list-func"),
    path("movies-func/<int:pk>/", movie_detail, name="movie-detail-func"),

    # ——— класові/генеричні в’юхи ———
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    # ——— ViewSet-и (Movies, CinemaHalls) ———
    path("", include(router.urls)),
]

app_name = "cinema"
