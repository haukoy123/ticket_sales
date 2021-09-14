from rest_framework import serializers

from apps.company.models.stop_point import StopPoint




class StopPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = StopPoint
        fields = '__all__'

# class StopPointReadonlySerializer(serializers.ModelSerializer):
#     user = EmployeesSerializer(read_only=True)
#     class Meta:
#         model = Employees
#         fields = "__all__"

