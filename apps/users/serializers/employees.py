import json

from rest_framework import serializers
from rest_framework.response import Response
from apps.users.models import User, Employees
# from apps.users.models.employees import
from apps.users.serializers.user import UserReadOnlySerializer, UserSerializer
from datetime import datetime
from rest_framework import status




class EmployeesSerializer(serializers.ModelSerializer):
    account = UserSerializer()
    class Meta:
        model = Employees
        fields = "__all__"
        # exclude = ('email')

    def validate_date_birth(self, value):
        # if value > datetime.now().astimezone(pytz.timezone('Asia/Ho_Chi_Minh')):
        if value >= datetime.now().date():
            raise serializers.ValidationError("Ngay sinh phai nho hon ngay hien tai")

class EmployeesReadonlySerializer(serializers.ModelSerializer):
    account = UserReadOnlySerializer(read_only=True)
    class Meta:
        model = Employees
        fields = "__all__"
        # exclude = ['email']

    def validate_date_birth(self, value):
        # if value > datetime.now().astimezone(pytz.timezone('Asia/Ho_Chi_Minh')):
        if value >= datetime.now().date():
            raise serializers.ValidationError("Ngay sinh phai nho hon ngay hien tai")
