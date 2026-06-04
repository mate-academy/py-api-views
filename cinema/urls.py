from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

# Роутер для MovieViewSet
router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")

# Явне прив'язування дій (actions) для CinemaHallViewSet
cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create"
})
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    # Genres (APIView)
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    # Actors (GenericAPIView)
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    # CinemaHalls (GenericViewSet)
    path("cinema_halls/", cinema_hall_list, name="cinemahall-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinemahall-detail"),

    # Movies (ModelViewSet та Router)
    path("", include(router.urls)),
]

app_name = "cinema"
