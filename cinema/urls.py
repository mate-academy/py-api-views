from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreView, ActorView, CinemaHallView, MovieView

router = DefaultRouter()
router.register(r"movies", MovieView, basename="movie")
router.register(r"cinema_halls", CinemaHallView, basename="cinema_hall")

urlpatterns = [
    path("genres/", GenreView.as_view()),
    path("actors/", ActorView.as_view()),
    path("", include(router.urls)),
]


app_name = "cinema"
