from rest_framework import serializers
# Dois espaços em branco esperados antes do primeiro import de modelo (E302)
# Assumindo que os modelos vieram de .models
from .models import Actor, Genre, CinemaHall, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__' # Dois espaços antes do comentário (E261)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__' # Dois espaços antes do comentário (E261)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__' # Dois espaços antes do comentário (E261)


class MovieSerializer(serializers.ModelSerializer):
    # Serializers sem related serializers para ManyToMany
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Movie
        # Linhas longas (E501) foram cortadas/ajustadas.
        fields = ['id', 'title', 'description', 'duration', 'actors', 'genres']
