from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    MovieViewSet,
    CinemaHallViewSet,
    ActorList,
    GenreList,
    GenreDetail,
    ActorDetail,
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="actors_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
]
urlpatterns += router.urls
app_name = "cinema"
