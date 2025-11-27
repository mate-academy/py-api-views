from django.urls import path, include
from rest_framework import routers
from .views import (
    GenreList, 
    GenreDetail, 
    ActorList, 
    ActorDetail, 
    CinemaHallViewSet, 
    MovieViewSet
)

# Initialize Router for ViewSets
router = routers.DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    # Explicit paths for APIView (Genre)
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    # Explicit paths for GenericAPIView (Actor)
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    # Router paths for ViewSets (CinemaHall, Movie)
    path("", include(router.urls)),
]
