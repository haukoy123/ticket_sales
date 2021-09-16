from apps.users.filters import CustomerFilterSet
from apps.users.models import User, Employees
from apps.users.models.customer import Customer
from apps.users.serializers.customer import CustomerSerializer, CustomerReadOnlySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from core.permissions import AdminPermission, OperatingStaffPermission, TickerSellerPermission, DriverStaffPermission



class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerReadOnlySerializer
    permission_classes = [OperatingStaffPermission | AdminPermission]
    # serializer_detail_class = CustomerReadOnlySerializer
    filterset_class = CustomerFilterSet

    def get_queryset(self):
        if self.permission_classes is AdminPermission:
            return Customer.objects.all()
        else:
            return Customer.objects.filter(account__in=User.objects.prefetch_related('tickets').filter(tickets__trip__vehicle__company_id=Employees.objects.get(account=self.request.user).company_id))








