from django.urls import path, include

from rest_framework import routers

from cinema.views import MovieViewSet, GenreList, GenreDetail

router = routers.DefaultRouter()
router.register("movie", MovieViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
]

app_name = "cinema"
