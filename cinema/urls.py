from django.urls import path

from cinema.views import GenreList, GenreDetail, ActorList

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
]

app_name = "cinema"
