from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.company.models.route import Route

class StopPointStatus(models.TextChoices):
    ACTIVATE = "ACTIVATE", _("ACTIVATE")
    INACTIVE = "INACTIVE", _("INACTIVE")

class StopPoint(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=StopPointStatus.choices, max_length=20, default=StopPointStatus.ACTIVATE)

    def __str__(self):
        # return self.route.name, self.name
        return '{}, {}'.format(self.route.name, self.name)
    class Meta:
        db_table = 'stop_point'
        ordering = ['route']