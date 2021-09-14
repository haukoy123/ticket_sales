from django.contrib import admin
from apps.company.models.company import Company

# Register your models here.
from apps.company.models.company_route import CompanyRoute
from apps.company.models.route import Route
from apps.company.models.stop_point import StopPoint
from apps.company.models.vehicle import Vehicle

admin.site.register(Company)
admin.site.register(Vehicle)
admin.site.register(Route)
admin.site.register(StopPoint)
admin.site.register(CompanyRoute)
