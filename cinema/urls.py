from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema import views

router = DefaultRouter()
router.register("movies", views.MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", views.genre_list, name="genre-list"),
    path("genres/<int:pk>/", views.genre_detail, name="genre-detail"),
    path("actors/", views.ActorListViewSet.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        views.ActorDetailViewSet.as_view(),
        name="actor-detail"
    ),
    path("hall/",
         views.CinemaHallViewSet.as_view(actions={
             "get": "list",
             "post": "create",
         }),
         name="hall-list"
         ),
    path("hall/<int:pk>/",
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
