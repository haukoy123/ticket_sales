from rest_framework import serializers
from apps.users.models.customer import Customer
from apps.users.serializers.user import UserReadOnlySerializer
from datetime import datetime
import pytz
from rest_framework.fields import CurrentUserDefault


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class CustomerReadOnlySerializer(serializers.ModelSerializer):
    account = UserReadOnlySerializer(read_only=True)
    class Meta:
        model = Customer
        exclude = []

    def validate_date_birth(self, value):
        # user = self.context.get('request')
        # print(user.user)
        # if value > datetime.now().astimezone(pytz.timezone('Asia/Ho_Chi_Minh')):
        if value >= datetime.now().date():
            raise serializers.ValidationError("Ngay sinh phai nho hon ngay hien tai")
