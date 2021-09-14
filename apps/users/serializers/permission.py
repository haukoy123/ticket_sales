
from rest_framework import serializers
from apps.users.models.permission import Permission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields ='__all__'