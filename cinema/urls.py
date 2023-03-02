from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, CinemaHallViewSet, ActorList, ActorDetail, GenreList, GenreDetail

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema-halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail")
]

app_name = "cinema"
