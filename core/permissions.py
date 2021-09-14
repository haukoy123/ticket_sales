from rest_framework.permissions import BasePermission
from  rest_framework.response import Response
from apps.users.models import Customer, Employees


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        # if isinstance(request.user, User):
        if request.user.permission.name == 'admin':
            return True
        return False


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, Customer):
            if request.user.permission.name == 'khachhang':
                return True
        return False


class TickerSellerPermission(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, Employees):
            if request.user.permission.name == 'nhanvienbanve':
                return True
        return False


class DriverStaffPermission(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, Employees):
            if request.user.permission.name == 'nhanvienxe':
                return True
        return False


class OperatingStaffPermission(BasePermission):
    def has_permission(self, request, view):
        if isinstance(check_user(request), Employees):
            if request.user.permission.name == 'nhanviendieuhanh':
                # print('a')
                return True
        return False

# def ktra(request):
#     if Employees.objects.filter(account=request.user).exists():
#         return Employees.objects.filter(account=request.user)
#     elif Customer.objects.filter(account=request.user).exists():
#         return Customer.objects.filter(account=request.user)
#     else:
#         return False

def check_user(request):
    try:
        return Employees.objects.get(account=request.user)
    except:
        try:
            return Customer.objects.get(account=request.user)
        except:
            return False