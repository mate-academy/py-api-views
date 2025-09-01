from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema-hall")

urlpatterns = [
    # FBV Movies
    path("movies-fbv/", movie_list, name="movie-list-fbv"),
    path("movies-fbv/<int:pk>/", movie_detail, name="movie-detail-fbv"),

    # APIView Genres
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    # GenericAPIView Actors
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    # Router handles both movies + cinema halls
    path("", include(router.urls)),
]

app_name = "cinema"
