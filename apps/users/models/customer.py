import uuid
from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteMixin
from .user import User
# from apps.users.models.user_manager import CustomUserManager

class UserGender(models.TextChoices):
    MALE = "MALE", _("MALE")
    FEMALE = "FEMALE", _("FEMALE")
    UNKNOWN = "UNKNOWN", _("UNKNOWN")


class Customer(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        choices=UserGender.choices,
        max_length=20,
        default=UserGender.UNKNOWN,
    )
    id_card = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.account.email

    # @property
    # def is_authenticated(self):
    #     return True
    class Meta:
        db_table = "customer"