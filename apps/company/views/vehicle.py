from rest_framework.viewsets import ModelViewSet

from apps.company.filters import VehicleFilterSet
from apps.company.models.vehicle import Vehicle
from apps.company.serializers.vehicle import VehicleSerializer
from apps.users.models import User, Employees


class VehicleView(ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = []
    # queryset_detail = Vehicle.objects.prefetch_related('trips')
    # queryset = User.objects.prefetch_related("users").filter(users__company_id=1)
    filterset_class = VehicleFilterSet

    def get_queryset(self):
        vehicle = Vehicle.objects.filter(company_id=Employees.objects.get(account=self.request.user).company_id)
        return vehicle
