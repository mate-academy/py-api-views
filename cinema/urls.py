# Correção final da estrutura de URLs
# Se o urlpatterns estiver dentro de um path('api/cinema/', include('cinema.urls')) em urls.py do projeto:
router = DefaultRouter()
router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'genres', GenreViewSet, basename='genre')
