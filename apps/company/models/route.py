from django.db import models
from django.utils.translation import gettext_lazy as _



class Route(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    province_begins = models.CharField(max_length=50, null=True, blank=True)
    province_ends = models.CharField(max_length=50, null=True, blank=True)
    departure_time = models.TimeField(null=True, blank=True)
    time_ends = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'route'