from django.urls import path

from cinema.views import GenreList, GenreDetail

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
]

app_name = "cinema"
