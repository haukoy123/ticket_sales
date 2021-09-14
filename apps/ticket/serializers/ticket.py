from rest_framework.serializers import ModelSerializer, ValidationError

from apps.ticket.models.ticket import Ticket
from apps.ticket.models.trip import Trip
from apps.users.models import Employees
from django.db.models import Count, Sum


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        exclude = []

    def validate_number_seat(self, value):
        request = self.context.get('request')
        trip_id = request.data['trip']
        trip = Trip.objects.prefetch_related('tickets').filter(id=trip_id)\
            .values('id', 'vehicle__number_seat').annotate(booked_chair=Sum('tickets__number_seat')).order_by('id').first()
        seat_ticket = 0
        if request.method == 'PUT':
            seat_ticket = Ticket.objects.get(id=request.parser_context['kwargs']['pk']).number_seat
        emty_seat = trip['vehicle__number_seat'] - trip['booked_chair'] + seat_ticket
        if value > emty_seat:
            raise ValidationError("not enough empty seats")
        return value
