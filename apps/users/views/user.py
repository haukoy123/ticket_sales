from datetime import datetime, timedelta
from django.db import transaction
from rest_framework.views import APIView
import jwt
from apps.users.models import User, Employees, Customer
from apps.users.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, status, exceptions

from apps.users.serializers.customer import CustomerSerializer
from apps.users.serializers.employees import EmployeesSerializer, EmployeesReadonlySerializer
from apps.users.serializers.user import LoginReadOnlySerializer, UserReadOnlySerializer, AddCustomerSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException

from core.mixins import GetSerializerClassMixin


class UserLoginView(APIView):
    permission_classes = []
    serializer_class = LoginReadOnlySerializer

    def post(self, request):
        serializer = LoginReadOnlySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = authenticate(
            request,
            username=username,
            password=password
        )
        iat = datetime.now()
        exp = iat + timedelta(days=60)
        payload = {
            "id": str(user.id),
            "exp": exp,
            "iat": iat,
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode("utf-8")
        return Response({'token': token})


class UserView(ModelViewSet):
    permission_classes = []
    serializer_action_classes = {
        "employees": EmployeesReadonlySerializer,
        "customer": CustomerSerializer,
        "list": UserSerializer,
        "retrieve": UserReadOnlySerializer,
    }
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(
        methods=["GET"],
        detail=False,
        url_path="me",
        url_name="me",
    )
    def me(self, request, *args, **kwargs):
        # user = request.user
        empl = Employees.objects.get(account_id=request.user.id)
        serializer = self.serializer_action_classes.get("employees")(
            empl
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[],
        serializer_class= LoginReadOnlySerializer,
        url_path="login",
        url_name="login",
    )
    def login(self, request, *args, **kwargs):
        serializer = LoginReadOnlySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        try:
            user = authenticate(
                request,
                username=username,
                password=password
            )
        except exceptions.NotFound:
            raise APIException(
                _("Email or password is wrong"),
                status.HTTP_404_NOT_FOUND,
            )
        iat = datetime.now()
        exp = iat + timedelta(days=60)
        payload = {
            "id": str(user.id),
            "exp": exp,
            "iat": iat,
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode("utf-8")
        return Response({'token': token})


    @action(
        methods=["POST"],
        detail=False,
        url_path="register",
        url_name="register",
        permission_classes=[],
        pagination_class=None,
    )
    def register(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data["password"]
        email = serializer.validated_data['email']
        try:
            user = User()
            user.email = email
            user.set_permission('khachhang')
            user.set_password(password)
            user.save()
            Customer.objects.create(account=user, email=email)
        except:
            raise APIException(_("Cannot register user"), status.HTTP_500_INTERNAL_SERVER_ERROR)

        token = user.token
        data = {"token": token}
        return Response(data=data, status=status.HTTP_200_OK)










