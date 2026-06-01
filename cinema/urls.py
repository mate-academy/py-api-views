from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"
router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    # Genre - APIView
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<pk>/", GenreDetail.as_view(), name="genre-detail"),

    # Actor - GenericAPIView
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls)),
]
