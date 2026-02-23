from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets

from django.shortcuts import get_object_or_404

from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
