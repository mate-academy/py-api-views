from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Genre endpoints using APIView
    path("cinema/genres/", GenreList.as_view(), name="genre-list"),
    path(
        "cinema/genres/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    # Actor endpoints using GenericAPIView
    path("cinema/actors/", ActorList.as_view(), name="actor-list"),
    path(
        "cinema/actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    # CinemaHall and Movie endpoints using ViewSets and router
    path("cinema/", include(router.urls)),
]

app_name = "cinema"
