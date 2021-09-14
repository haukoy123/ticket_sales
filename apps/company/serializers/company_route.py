from rest_framework import serializers

from apps.company.models.company_route import CompanyRoute


class CompanyRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyRoute
        fields = '__all__'

# class CompanyRouteReadonlySerializer(serializers.ModelSerializer):
#     user = EmployeesSerializer(read_only=True)
#     class Meta:
#         model = Employees
#         fields = "__all__"

