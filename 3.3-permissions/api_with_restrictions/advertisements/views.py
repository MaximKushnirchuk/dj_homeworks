from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.response import Response


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []


@api_view(["GET"])
def sample_view(request):
    return Response("Hello")
