from django.urls import path, include
from rest_framework import routers
from cinema.views import GenreList, GenreDetail, ActorList, ActorDetail, CinemaHallViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path("genres/", GenreList.as_view()),
    path("genres/<int:pk>/", GenreDetail.as_view()),
    path("actors/", ActorList.as_view()),
    path("actors/<int:pk>/", ActorDetail.as_view()),
    path("cinema_halls/", CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view(actions={"get": "retrieve", "put": "update",
                                                                      "patch": "partial_update", "delete": "destroy"})),
    path('', include(router.urls))

]

app_name = "cinema"
