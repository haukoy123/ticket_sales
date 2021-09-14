from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["deleted", 'is_superuser', 'last_login']
        read_only_fields = ["created_at", "updated_at", 'last_login']
        # extra_kwargs = {
        #     'email': {'validators': []},
        # }

        # extra_kwargs = {'password': {'write_only': True}}



class UserReadOnlySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    permission_id = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class LoginReadOnlySerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class AddCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["deleted", 'is_superuser', 'last_login', 'permission']
        # read_only_fields = ["created_at", "updated_at", 'last_login']