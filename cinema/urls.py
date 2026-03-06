from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    movie_list,
    movie_detail,
    MovieViewSet,
    ActorList,
    ActorDetail,
    GenreList,
    GenreDetail,
    CinemaHallViewSet
)

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("", include(router.urls), name="set-view"),

]

app_name = "cinema"
