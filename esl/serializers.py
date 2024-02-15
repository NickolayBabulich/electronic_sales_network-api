from rest_framework import serializers
from esl.models import Supplier, CommercialNetwork


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class CommercialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommercialNetwork
        fields = '__all__'
