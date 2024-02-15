import django_filters
from esl.models import Supplier, CommercialNetwork


class SellerFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = Supplier
        fields = ("country",)


class NetworkFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = CommercialNetwork
        fields = ("country",)
