from rest_framework import routers
from django.urls import path, include

from cinema.views import (
    MovieViewSet,
    GenerDetail,
    GenreList
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenerDetail.as_view(), name="genres-detail")
]

app_name = "cinema"
