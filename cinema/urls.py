from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList,
    GenreDetail,
    CinemaHallViewSet,
    ActorList,
    ActorDetail,
    MovieViewSet
)


router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),
    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),
    path("", include(router.urls)),
]

app_name = "cinema"
