from rest_framework import serializers

from apps.company.models.vehicle import Vehicle
from core.utils import validate_positive


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


    def validate_number_seat(self, value):
        return validate_positive(value, "number_seat")

# class VehicleReadonlySerializer(serializers.ModelSerializer):
#     # user = EmployeesSerializer(read_only=True)
#     class Meta:
#         model = Vehicle
#         fields = "__all__"

