from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.ticket.models.trip import Trip
from apps.users.models import User

class TicketStatus(models.TextChoices):
    CANCELL = "CANCELL", _("CANCELL")
    INCOMPLETE = "INCOMPLETE", _("INCOMPLETE")
    COMPLETE = "COMPLETE", _("COMPLETE")


class Ticket(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='tickets')
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    name_customer = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    time_booked = models.DateTimeField(null=True, blank=True)
    destination = models.TextField(max_length=100, null=True, blank=True)
    number_seat = models.IntegerField(null=True, blank=True)
    total_money = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=TicketStatus.choices, max_length=20, default=TicketStatus.INCOMPLETE)


    def __str__(self):
        return self.name_customer
    class Meta:
        db_table = 'ticket'
        ordering = ['id']