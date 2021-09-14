from django.contrib import admin
from .models import User, Permission, Customer, Employees


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Employees)
admin.site.register(Customer)
admin.site.register(Permission)
