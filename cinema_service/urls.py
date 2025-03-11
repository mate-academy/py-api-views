from django.urls import include, path

urlpatterns = [
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
]
