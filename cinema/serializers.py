from rest_framework import serializers
from .models import Actor, Genre, CinemaHall, Movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__' # Ou ['id', 'first_name', 'last_name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__' # Ou ['id', 'name']

class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__' # Ou ['id', 'name', 'rows', 'seats_in_row']

class MovieSerializer(serializers.ModelSerializer):
    # Serializers sem related serializers para ManyToMany
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'actors', 'genres']
