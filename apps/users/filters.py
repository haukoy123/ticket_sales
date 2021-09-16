import django_filters

from core.filters import CaseInsensitiveOrderingFilter



class CustomerFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains",
                                         field_name="name")

    email = django_filters.CharFilter(lookup_expr="icontains",
                                      field_name="email")

    gender = django_filters.CharFilter(lookup_expr="iexact",
                                           field_name="gender")

    phone = django_filters.CharFilter(lookup_expr="icontains",
                                           field_name="phone")

    ordering = django_filters.OrderingFilter(fields=("date_birth", "username"))



class EmployeesFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains",
                                         field_name="name")

    email = django_filters.CharFilter(lookup_expr="icontains",
                                      field_name="email")

    gender = django_filters.CharFilter(lookup_expr="iexact",
                                           field_name="gender")

    phone = django_filters.CharFilter(lookup_expr="icontains",
                                           field_name="phone")

    permission = django_filters.CharFilter(lookup_expr="icontains",
                                           field_name="permission__name")

    ordering = django_filters.OrderingFilter(fields=("date_birth", "username"))




class UserFilterSet(django_filters.FilterSet):

    username = django_filters.CharFilter(lookup_expr="icontains",
                                     field_name="username")

    email = django_filters.CharFilter(lookup_expr="icontains",
                                      field_name="email")

    position = django_filters.CharFilter(lookup_expr="iexact",
                                      field_name="account__permission__name")

    ordering = django_filters.OrderingFilter(fields=("created_at",
                                                     "updated_at", "username"))

    # class Meta:
    #     model = User
    #     fields = {
    #         'username': ['exact', 'contains'],
    #         'last_login': ['exact', 'year__gt'],
    #     }


class StaffFilterSet(django_filters.FilterSet):
    channel = django_filters.UUIDFilter(field_name="channel_id")
    user = django_filters.UUIDFilter(field_name="user_id")
    roles = django_filters.CharFilter(field_name="roles",
                                      method="role_ids_filter")
    name = django_filters.CharFilter(lookup_expr="icontains",
                                     field_name="name")
    email = django_filters.CharFilter(lookup_expr="icontains",
                                      field_name="email")
    ordering = CaseInsensitiveOrderingFilter(
        fields=("created_at", "updated_at", "name"),
        case_insensitive_fields=["name"],
    )

    def role_ids_filter(self, queryset, name, value):
        ids = value.split(",")
        return queryset.filter(role__id__in=ids)


class RoleFilterSet(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name")


class InviteUrlFilterSet(django_filters.FilterSet):
    creator = django_filters.UUIDFilter(field_name="creator_id")
    role_ids = django_filters.CharFilter(field_name="role_ids",
                                         method="role_ids_filter")

    def role_ids_filter(self, queryset, name, value):
        ids = value.split(",")
        return queryset.filter(role__id__in=ids)
