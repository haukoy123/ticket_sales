from rest_framework import serializers

from apps.company.models.route import Route
from apps.company.models.stop_point import StopPoint
from apps.company.serializers.stop_point import StopPointSerializer


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

# class RouteReadonlySerializer(serializers.ModelSerializer):
#     stoppoint = StopPointSerializer(read_only=True)
#     class Meta:
#         model = Route
#         exclude = []

