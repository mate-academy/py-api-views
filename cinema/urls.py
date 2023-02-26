from django.urls import path
from rest_framework import routers

from cinema.views import GenreList, GenreDetail, MovieViewSet, ActorList, \
    ActorDetail

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    # path("actors/", ActorList.as_view(), name="genre-detail"),
    # path("genres/<int:pk>/", ActorDetail.as_view(), name="genre-detail"),

    # path("movies/", MovieViewSet.as_view(), name="movie-list"),
    # path("movies/<int:pk>/", MovieViewSet.as_view(), name="movie-detail"),
]

app_name = "cinema"
