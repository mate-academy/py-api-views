from django.urls import path

from cinema.views import (
    GenreAPIView,
    GenreDetailAPIView,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register(r"movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
]

urlpatterns += router.urls

app_name = "cinema"
