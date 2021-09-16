from rest_framework.response import Response
from rest_framework import status

from apps.users.filters import EmployeesFilterSet
from apps.users.models import User
from apps.users.models.employees import Employees
from apps.users.serializers.employees import EmployeesSerializer, EmployeesReadonlySerializer
from rest_framework.viewsets import ModelViewSet
from core.permissions import AdminPermission, OperatingStaffPermission, TickerSellerPermission, DriverStaffPermission
from django.forms.models import model_to_dict


class EmployeesViewSet(ModelViewSet):
    permission_classes = [OperatingStaffPermission | AdminPermission]
    serializer_class = EmployeesReadonlySerializer
    # allowed_methods = ('GET',)
    filterset_class = EmployeesFilterSet


    def get_queryset(self):
        if self.permission_classes is AdminPermission:
            return Employees.objects.all()
        else:
            return Employees.objects.filter(company_id=Employees.objects.get(account=self.request.user).company_id)



    def create(self, request, *args, **kwargs):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.pop('account')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        usernew = User.objects.create(**user)
        instance = Employees.objects.create(account=usernew, **serializer.validated_data)
        data = EmployeesReadonlySerializer(instance)
        # model_to_dict(instance)
        headers = self.get_success_headers(data.data)
        return Response(data.data, status=status.HTTP_201_CREATED, headers=headers)

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = EmployeesSerializer(instance, data=request.data, partial=partial)
    #     if serializer.is_valid():
    #         account = serializer.validated_data.pop('account')
    #         serializer.fields['account'].update(instance.account, account)
    #
    #         # empl = Employees.objects.filter(id=instance.id)
    #         # employees = empl.update(**serializer.validated_data)
    #         serializer.save()
    #         # employees = EmployeesUpdate(instance, data=request.data, partial=partial)
    #         # employees.is_valid(raise_exception=True)
    #         # employees.save()
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(serializer.data)