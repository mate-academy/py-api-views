from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList, GenreDetail,
    ActorList, ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("api/cinema/genres/", GenreList.as_view()),
    path("api/cinema/genres/<int:pk>/", GenreDetail.as_view()),
    path("api/cinema/actors/", ActorList.as_view()),
    path("api/cinema/actors/<int:pk>/", ActorDetail.as_view()),
    path("api/cinema/", include(router.urls)),
]

app_name = "cinema"
