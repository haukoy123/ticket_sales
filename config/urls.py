from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from apps.company.views.company import CompanyView
from apps.company.views.company_route import CompanyRouteView
from apps.company.views.route import RouteView
from apps.company.views.stop_point import StopPointView
from apps.company.views.vehicle import VehicleView
from apps.ticket.views.ticket import TicketView
from apps.ticket.views.trip import TripView
from apps.users.views import UserView
from rest_framework.routers import SimpleRouter



import rest_framework
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


swagger_info = openapi.Info(
    title="Eureka API",
    default_version="v1",
    description="""Eureka project.""",
    contact=openapi.Contact(email="hautran2699@gmail.com"),
    license=openapi.License(name="Private"),
)

schema_view = get_schema_view(
    info=swagger_info,
    public=True,
    authentication_classes=[
        rest_framework.authentication.SessionAuthentication
    ],
    permission_classes=[permissions.IsAdminUser],
)
from apps.users.views.customer import CustomerViewSet
from apps.users.views.employees import EmployeesViewSet

api_router = SimpleRouter(trailing_slash=False)
api_router.register("user", UserView, basename="user")
api_router.register("employees", EmployeesViewSet, basename="employees")
api_router.register("customers", CustomerViewSet, basename="customers")
api_router.register("companies", CompanyView, basename="companies")
api_router.register("vehicles", VehicleView, basename="vehicles")
api_router.register("routes", RouteView, basename="routes")
api_router.register("stop_point", StopPointView, basename="stop_point")
api_router.register("company_route", CompanyRouteView, basename="company_route")
api_router.register("trips", TripView, basename="trips")
api_router.register("tickets", TicketView, basename="tickets")



admin.autodiscover()


# from apps.users.views.user import showuser

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"api/v1/", include(api_router.urls)),
    # path("index/", showuser , name ='index'),
]

urlpatterns.extend([
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
])