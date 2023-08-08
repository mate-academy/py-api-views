from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register(r"cinema_halls", CinemaHallViewSet)
router.register(r"movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("/", include(router.urls)),
]
urlpatterns += router.urls
