from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def root_view(request):
    return HttpResponse(
        "Welcome to the Cinema API! Use /api/cinema/ to access the endpoints.",
        content_type="text/plain")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("", root_view),
]
