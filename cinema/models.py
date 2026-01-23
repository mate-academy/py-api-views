# No seu models.py
class Movie(models.Model):
    # ... outros campos
    actors = models.ManyToManyField(Actor, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    # ...
