from rest_framework.viewsets import ModelViewSet

from apps.company.models.company_route import CompanyRoute
from apps.company.serializers.company_route import CompanyRouteSerializer
from apps.users.models import Employees
from core.permissions import OperatingStaffPermission, AdminPermission


class CompanyRouteView(ModelViewSet):
    serializer_class = CompanyRouteSerializer
    # queryset = CompanyRoute.objects.all()
    permission_classes = [OperatingStaffPermission | AdminPermission]


    def get_queryset(self):
        if self.request.user.permission.name == 'admin':
            return CompanyRoute.objects.all()
        else:
            return CompanyRoute.objects.filter(company_id=Employees.objects.get(account=self.request.user).company_id)


