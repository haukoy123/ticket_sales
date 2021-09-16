import django_filters


class VehicleFilterSet(django_filters.FilterSet):
    liceicnse_plates = django_filters.CharFilter(lookup_expr="icontains",
                                         field_name="liceicnse_plates")

    color = django_filters.CharFilter(lookup_expr="iexact",
                                      field_name="color")

    type = django_filters.CharFilter(lookup_expr="iexact",
                                         field_name="vehicle_type")

    number_seat = django_filters.CharFilter(lookup_expr="iexact",
                                         field_name="number_seat")


    ordering = django_filters.OrderingFilter(fields=("number_seat"))




class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains",
                                         field_name="name")

    phone = django_filters.CharFilter(lookup_expr="icontains",
                                      field_name="phone")

    email = django_filters.CharFilter(lookup_expr="icontains",
                                         field_name="email")


    ordering = django_filters.OrderingFilter(fields=("name"))