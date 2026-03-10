from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import GenreList, GenreDetail, ActorList, MovieViewSet, CinemaViewSet, ActorDetail

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaViewSet)

urlpatterns = [
    # Genre - APIView
    path("cinema/genres/", GenreList.as_view()),
    path("cinema/genres/<int:pk>/", GenreDetail.as_view()),

    # Actor - GenericAPIView
    path("cinema/actors/", ActorList.as_view()),
    path("cinema/actors/<int:pk>/", ActorDetail.as_view()),

    # CinemaHall і Movie - через router
    path("cinema/", include(router.urls)),
]

app_name = "cinema"

