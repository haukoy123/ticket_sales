from rest_framework.viewsets import ModelViewSet

from apps.company.models.route import Route
from apps.company.serializers.route import RouteSerializer


class RouteView(ModelViewSet):
    permission_classes = []
    serializer_class = RouteSerializer
    queryset = Route.objects.all()
