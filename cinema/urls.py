from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cinema import views

app_name = "cinema"

router = DefaultRouter()
router.register("movies", views.MovieViewSet, basename="movie")
router.register("cinema_halls", views.CinemaHallViewSet,
                basename="cinema_hall")

urlpatterns = [
    path("genres/", views.GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", views.GenreDetail.as_view(), name="genre-detail"),
    path("actors/", views.ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", views.ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls)),
]
