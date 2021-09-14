from rest_framework.viewsets import ModelViewSet

from apps.company.models.stop_point import StopPoint
from apps.company.serializers.stop_point import StopPointSerializer


class StopPointView(ModelViewSet):
    permission_classes = []
    serializer_class = StopPointSerializer
    # queryset = StopPoint.objects.filter(id=1)
    queryset = StopPoint.objects.all()