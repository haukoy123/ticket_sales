from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.company.models.company import Company
from apps.company.serializers.company import CompanySerializer
from apps.users.models import Employees
from apps.users.serializers import UserSerializer
from rest_framework import status
from core.permissions import AdminPermission, OperatingStaffPermission, TickerSellerPermission, DriverStaffPermission



class CompanyView(ModelViewSet):
    permission_classes = [AdminPermission]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    # allowed_methods = ('GET', 'PUT', 'POST')

    def create(self, request, *args, **kwargs):
        company = CompanySerializer(data=request.data)
        company.is_valid(raise_exception=True)
        # company.save()
        self.perform_create(company)
        user = UserSerializer(data=request.data['account'])
        user.is_valid(raise_exception=True)
        # user.save()
        self.perform_create(user)

        employees = Employees(company_id=company.data.get("id"), account_id=user.data.get("id"))
        # employees.save()
        self.perform_create(employees)
        data = {"company": company.data, "user": user.data}
        headers = self.get_success_headers(data)
        return Response(data=data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # company = super(CompanyView, self).update(request, *args, **kwargs)
        company = CompanySerializer(instance=instance, data=request.data)
        company.is_valid(raise_exception=True)
        self.perform_update(company)
        # company.save()

        user = UserSerializer(instance=instance, data=request.data['account'])
        user.is_valid(raise_exception=True)
        # user.save()
        self.perform_update(user)
        return Response(data={"company": company.data,"user": user.data})
