from django.urls import path, include
from rest_framework import routers

from cinema.views import ActorList, ActorDetail, gernre_list, genre_detail, MovieViewSet

app_name = "cinema"

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")


urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("genres/", gernre_list, name="genre_list"),
    path("genres/<int:pk>/", genre_detail, name="genre_detail"),
    path("", include(router.urls), name="movie"),
]
