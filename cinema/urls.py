from django.urls import path
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreAPIView,
    ActorAPIView,
    CinemaHallViewSet,
    MovieViewSet,
)

app_name = "cinema"
router = DefaultRouter()
router.register("cinema-halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("genres/", GenreAPIView.as_view()),
    path("genres/<int:pk>/", GenreAPIView.as_view()),

    path("actors/", ActorAPIView.as_view()),
    path("actors/<int:pk>/", ActorAPIView.as_view()),
]

urlpatterns += router.urls
