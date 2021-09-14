from apps.users.models.permission import Permission
from apps.users.serializers.permission import PermissionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from core import permissions


class PermissionViewSet(ModelViewSet):
    permission_classes = []
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = []


    def get(self, request):
        queryset = self.queryset.all()
        if not request.user.is_superuser:
            queryset = queryset.exclude(is_superuser=True)
        # queryset = queryset.values()
        return queryset

    def post(self, request):
        da = PermissionSerializer(data=request.data)
        # ktra du lieu gui len co dung cau truc khong
        if not da.is_valid():
            return Response(da.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            da.save()
            return Response(da.data, status=status.HTTP_200_OK)