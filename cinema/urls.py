from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, ActorViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
