import pytz
from rest_framework import serializers

from apps.ticket.models.ticket import Ticket
from apps.users.models import Employees

timezone = pytz.timezone('Asia/Ho_Chi_Minh')


def localize_datetime(datetime):
    return timezone.localize(datetime)


def validate_positive(value, field):
    if value < 0:
        raise serializers.ValidationError(f"{field} must be positive".format(field=field))
    return value

def empty_seat():
    ticket = Ticket.objects.select_related("trip").filter(trip__vehicle__company_id=Employees.objects.get(account=self.request.user).company_id)
