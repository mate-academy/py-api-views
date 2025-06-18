from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreList, GenreDetail,
    ActorListCreate, ActorRetrieveUpdateDestroy,
    CinemaHallViewSet,
    MovieViewSet
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema_hall")

app_name = "cinema"

urlpatterns = [
    path("genres/", GenreList.as_view(),
         name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(),
         name="genre-detail"),
    path("actors/", ActorListCreate.as_view(),
         name="actor-list"),
    path("actors/<int:pk>/",
         ActorRetrieveUpdateDestroy.as_view(),
         name="actor-detail"),
    path("", include(router.urls)),
]
