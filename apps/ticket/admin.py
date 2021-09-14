from django.contrib import admin

# Register your models here.
from apps.ticket.models.ticket import Ticket
from apps.ticket.models.trip import Trip

admin.site.register(Trip)
admin.site.register(Ticket)