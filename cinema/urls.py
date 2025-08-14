from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateAPIView,
    GenreDetailAPIView,
    ActorListCreateAPIView,
    ActorDetailAPIView,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema_hall")

urlpatterns = [
    # Genres (APIView)
    path("api/cinema/genres/", GenreListCreateAPIView.as_view(),
         name="genre-list"),
    path("api/cinema/genres/<int:pk>/", GenreDetailAPIView.as_view(),
         name="genre-detail"),

    # Actors (GenericAPIView)
    path("api/cinema/actors/", ActorListCreateAPIView.as_view(),
         name="actor-list"),
    path("api/cinema/actors/<int:pk>/", ActorDetailAPIView.as_view(),
         name="actor-detail"),

    # ViewSets (CinemaHall + Movie) via router
    path("api/cinema/", include(router.urls)),
]
