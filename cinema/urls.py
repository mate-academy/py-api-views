from django.urls import path, include

from cinema.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("cinema_halls", CinemaHallViewSet)


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre_list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),
    path("actors/", ActorList.as_view(), name="genre_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="genre_detail"),
    path("", include(router.urls))

]

app_name = "cinema"
