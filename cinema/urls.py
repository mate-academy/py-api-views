from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, gernre_list, genre_detail

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")


urlpatterns = [
    path("", include(router.urls), name="movie"),
    path("genres/", gernre_list, name="genre_list"),
    path("genres/<int:pk>/", genre_detail, name="genre_detail"),
]
