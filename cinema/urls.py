from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import MovieViewSet, GenreViewSet, ActorViewSet, CinemaHallViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_hall")
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")

app_name = "cinema"
urlpatterns = [
    path('', include(router.urls)),
]
