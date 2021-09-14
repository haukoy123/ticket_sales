from django.db import models
from safedelete import NO_DELETE


class Permission(models.Model):
    _safedelete_policy = NO_DELETE
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'permission'