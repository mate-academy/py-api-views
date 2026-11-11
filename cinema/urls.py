from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema import views

router = DefaultRouter()
router.register("movies", views.MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", views.GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", views.GenreDetail.as_view(), name="genre-detail"),
    path("actors/", views.ActorList.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        views.ActorDetail.as_view(),
        name="actor-detail"
    ),
    path("cinema_halls/",
         views.CinemaHallViewSet.as_view(actions={
             "get": "list",
             "post": "create",
         }),
         name="hall-list"
         ),
    path("cinema_halls/<int:pk>/",
         views.CinemaHallViewSet.as_view(actions={
             "get": "retrieve",
             "put": "update",
             "patch": "partial_update",
             "delete": "destroy",
         }),
         name="hall-detail"
         ),
    path("", include(router.urls)),
]

app_name = "cinema"
