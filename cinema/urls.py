from django.urls import path, include
from rest_framework import routers

from cinema.views import ActorList, ActorDetail, GenreList, GenreDetail, MovieViewSet, CinemaHallViewSet

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("cinema-halls", CinemaHallViewSet, basename="cinema_hall")


urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("", include(router.urls),),
]
