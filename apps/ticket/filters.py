import django_filters

class TicketFilter(django_filters.FilterSet):
    trip = django_filters.CharFilter(lookup_expr="iexact",
                                     field_name="trip_id")

    account = django_filters.CharFilter(lookup_expr="icontains",
                                      field_name="account__email")

    ticket = django_filters.CharFilter(lookup_expr="iexact",
                                      field_name="id")

    phone = django_filters.CharFilter(lookup_expr="icontains",
                                      field_name="phone")

    total = django_filters.RangeFilter(field_name="total_money")

    seat = django_filters.RangeFilter(field_name="number_seat")

    time_booked = django_filters.DateFromToRangeFilter(field_name="time_booked")

    ordering = django_filters.OrderingFilter(fields=("number_seat","total_money",
                                                     "time_booked","trip_id","time_booked"))



class TripFilter(django_filters.FilterSet):
    trip = django_filters.CharFilter(lookup_expr="iexact",
                                     field_name="id")

    route = django_filters.CharFilter(lookup_expr="iexact",
                                      field_name="company_route__route__name")

    vehicle = django_filters.CharFilter(lookup_expr="icontains",
                                      field_name="vehicle__liceicnse_plates")

    departure_day = django_filters.DateFromToRangeFilter(field_name="time_booked")


    ordering = django_filters.OrderingFilter(fields=("vehicle","company_route","departure_day"))

