from rest_framework import serializers

from apps.company.models.company import Company
from apps.users.models import Employees
from apps.users.serializers.employees import EmployeesSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyReadonlySerializer(serializers.ModelSerializer):
    user = EmployeesSerializer(read_only=True)
    class Meta:
        model = Employees
        fields = "__all__"

