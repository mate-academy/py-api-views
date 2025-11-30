from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    GenreListAPIView,
    GenreDetailAPIView,
    ActorListCreateView,
    ActorDetailView,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"

# ---- Routers para ViewSets ----
router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls")
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    # Genre – APIView
    path("genres/", GenreListAPIView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),

    # Actor – GenericAPIView
    path("actors/", ActorListCreateView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),

    # ViewSets (CinemaHall + Movie)
    path("", include(router.urls)),
]
