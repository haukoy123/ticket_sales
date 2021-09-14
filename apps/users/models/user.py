import uuid
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import jwt
from django.db import models
from safedelete import HARD_DELETE
from safedelete.models import SafeDeleteMixin
from apps.users.models.permission import Permission


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=email, is_superuser=True, **kwargs)
        user.set_password(password)
        user.set_permission('admin')
        user.save(using=self._db)
        return user

class User(SafeDeleteMixin, AbstractBaseUser):
    # Delete not use field
    _safedelete_policy = HARD_DELETE
    USERNAME_FIELD = "email"
    objects = UserManager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    permission = models.ForeignKey(Permission, null=True, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def token(self):
        return self._generate_jwt_token()

    def clean(self):
        super().clean()

    def _generate_jwt_token(self):
        iat = datetime.now()
        exp = iat + timedelta(days=60)
        payload = {
            "id": str(self.id),
            "email": self.email,
            "exp": exp,
            "iat": iat,
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        return token.decode("utf-8")


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = "user"
        ordering = ["email"]

    def has_admin_permission(self):
        return self.permission.name == "admin"

    def set_permission(self, permission):
        if permission == 'admin':
            permission = Permission.objects.get(name="admin")
        elif permission =='nhanvienbanve':
            permission = Permission.objects.get(name="nhanvienbanve")
        elif permission == 'nhanviendieuhanh':
            permission = Permission.objects.get(name="nhanviendieuhanh")
        elif permission == 'nhanvienxe':
            permission = Permission.objects.get(name="nhanvienxe")
        else:
            permission = Permission.objects.get(name="khachhang")
        print(permission.name)
        if permission is not None:
            self.permission = permission
            # self.save()