from django.urls import path, include

from rest_framework import routers

from cinema.views import GenreList, GenreDetail, ActorList, ActorDetail, \
    CinemaHallViewSet, MovieViewSet


router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
]

app_name = "cinema"
