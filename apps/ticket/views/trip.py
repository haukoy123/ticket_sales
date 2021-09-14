from rest_framework.viewsets import ModelViewSet

from apps.ticket.models.trip import Trip
from apps.ticket.serializers.trip import TripSerializer
from apps.users.models import Employees
from core.permissions import AdminPermission, OperatingStaffPermission, TickerSellerPermission, DriverStaffPermission


class TripView(ModelViewSet):
    permission_classes = [OperatingStaffPermission | TickerSellerPermission | DriverStaffPermission]
    serializer_class = TripSerializer

    def get_queryset(self):
        trip = Trip.objects.select_related("vehicle").filter(vehicle__company_id=Employees.objects.get(account=self.request.user).company_id)
        return trip
