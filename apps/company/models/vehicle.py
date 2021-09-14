from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.company.models.company import Company


class VehicleType(models.TextChoices):
    Sleeping = "Sleeping car", _("Sleeping car")
    Normal = "Normal car", _("Normal car")

class VehicleStatus(models.TextChoices):
    ACTIVATE = "ACTIVATE", _("ACTIVATE")
    INACTIVE = "INACTIVE", _("INACTIVE")


class Vehicle(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    liceicnse_plates = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    vehicle_type = models.CharField(max_length=100, choices=VehicleType.choices, default=VehicleType.Normal)
    number_seat = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=VehicleStatus.choices,  max_length=20, default=VehicleStatus.ACTIVATE)

    def __str__(self):
        return self.liceicnse_plates
    class Meta:
        db_table = 'vehicle'
        ordering = ['company']