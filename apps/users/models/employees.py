from django.db import models
from django.utils.translation import gettext_lazy as _
from .user import User
from ...company.models.company import Company


class UserGender(models.TextChoices):
    MALE = "MALE", _("MALE")
    FEMALE = "FEMALE", _("FEMALE")
    UNKNOWN = "UNKNOWN", _("UNKNOWN")

class UserTeam(models.TextChoices):
    Manager = "Manager", _("Manager")
    Ticket = "Ticket Team", _("Ticket Team")
    Driver = "Driver team", _("Driver team")



class Employees(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    date_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        choices=UserGender.choices,
        max_length=20,
        default=UserGender.UNKNOWN,
    )
    id_card = models.CharField(max_length=100, null=True, blank=True)
    team = models.CharField(max_length=100, null=True, blank=True)



    # def team(self):


    def __str__(self):
        return self.account.email
    class Meta:
        db_table = "employees"
        ordering = ['id']