from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreAPIView,
    ActorGenericAPIView,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    # Genre (APIView)
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreAPIView.as_view(), name="genre-detail"),

    # Actor (GenericAPIView)
    path("actors/", ActorGenericAPIView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorGenericAPIView.as_view(), name="actor-detail"),

    # ViewSets
    path("", include(router.urls)),
]
