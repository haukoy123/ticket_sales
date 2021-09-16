from rest_framework.viewsets import ModelViewSet

from apps.ticket.filters import TicketFilter
from apps.ticket.models.ticket import Ticket
from apps.ticket.serializers.ticket import TicketSerializer
from apps.users.models import Employees
from core.mixins import GetSerializerClassMixin
from core.permissions import AdminPermission, OperatingStaffPermission, TickerSellerPermission, DriverStaffPermission
from rest_framework.permissions import AllowAny, IsAuthenticated

class TicketView(GetSerializerClassMixin,ModelViewSet):
    permission_classes = [OperatingStaffPermission | TickerSellerPermission]
    serializer_class = TicketSerializer
    # queryset = Ticket.objects.all()
    filterset_class= TicketFilter

    def get_queryset(self):
        ticket = Ticket.objects.select_related("trip").filter(trip__vehicle__company_id=Employees.objects.get(account=self.request.user).company_id)
        return ticket

