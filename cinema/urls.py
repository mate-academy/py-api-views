from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet

router = routers.SimpleRouter()
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls), name="movies")
]

app_name = "cinema"
