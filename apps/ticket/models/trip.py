from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.company.models.company_route import CompanyRoute
from apps.company.models.vehicle import Vehicle


class TripStatus(models.TextChoices):
    ACTIVATE = "ACTIVATE", _("ACTIVATE")
    INACTIVE = "INACTIVE", _("INACTIVE")
    COMPLETE = "COMPLETE", _("COMPLETE")

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="trips")
    company_route = models.ForeignKey(CompanyRoute, on_delete=models.CASCADE, related_name="trips"),
    name = models.CharField(max_length=50, null=True, blank=True)
    departure_day = models.DateField(null=True, blank=True)
    status = models.CharField(
        choices=TripStatus.choices,
        max_length=20,
        default=TripStatus.ACTIVATE,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'trip'
        ordering = ['id']
