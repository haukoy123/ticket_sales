from rest_framework.serializers import ModelSerializer, ValidationError
from datetime import datetime
from apps.ticket.models.trip import Trip


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        exclude = []

    def validate_departure_day(self, value):
        if value <= datetime.now().date():
            raise ValidationError("ngay di phai lon hon ngay hien tai")