from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreAPIView,
    ActorGenericAPIView,
    CinemaHallGenericViewSet,
    MovieModelViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("cinema_halls", CinemaHallGenericViewSet)
router.register("movies", MovieModelViewSet)

urlpatterns = [
    path("genres/", GenreAPIView.as_view()),
    path("genres/<int:pk>/", GenreAPIView.as_view()),

    path("actors/", ActorGenericAPIView.as_view()),
    path("actors/<int:pk>/", ActorGenericAPIView.as_view()),

    path("", include(router.urls)),
]
