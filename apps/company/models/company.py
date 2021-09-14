from django.db import models
from django.utils.translation import gettext_lazy as _


class CompanyStatus(models.TextChoices):
    ACTIVATE = "ACTIVATE", _("ACTIVATE")
    INACTIVE = "INACTIVE", _("INACTIVE")


class Company(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(
        choices=CompanyStatus.choices,
        max_length=20,
        default=CompanyStatus.ACTIVATE,
    )
    def __str__(self):
        return self.name

    class Meta:
        db_table = "company"
        ordering = ['id']
