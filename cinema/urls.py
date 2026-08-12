from django.urls import path, include
from cinema.views import CinemaHallViewSet, GenreList, GenreDetail, ActorList, ActorDetail,  MovieViewSet
from rest_framework import routers


app_name = "cinema"

router = routers.DefaultRouter()

router.register("cinema_halls", CinemaHallViewSet)

router.register("movies", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

]
