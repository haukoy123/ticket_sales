from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.company.models.company import Company
from apps.company.models.route import Route


class CompanyRouteStatus(models.TextChoices):
    ACTIVATE = "ACTIVATE", _("ACTIVATE")
    INACTIVE = "INACTIVE", _("INACTIVE")

class CompanyRoute(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    status = models.CharField(
        choices=CompanyRouteStatus.choices,
        max_length=20,
        default=CompanyRouteStatus.ACTIVATE,
    )
    def __str__(self):
        return '{}, {}'.format(self.company.name, self.route)
    class Meta:
        db_table = "company_route"
        ordering = ['company']
