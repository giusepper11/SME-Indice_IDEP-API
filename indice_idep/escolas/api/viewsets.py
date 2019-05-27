import django_filters
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet

from escolas.models import Escolas
from .serializers import EscolasSerializer


class EscolasViewSet(ReadOnlyModelViewSet):
    """
    Endpoint responsável por retornar todas as escolas,
    filtrar pro Codigo da escola ou realizar pesquisa por nome da escola
    """
    queryset = Escolas.objects.exclude(tipoesc='ESC.PART.')
    serializer_class = EscolasSerializer
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    search_fields = ('nomesc',)
    filterset_fields = ('dre', 'tipoesc', 'distrito', 'bairro')
