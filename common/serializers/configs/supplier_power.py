from rest_framework import serializers
from common.models.general import SupplierPower


class SupplierPowerSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='SupplierPowerId')

    class Meta:
        model = SupplierPower
        fields = ('label', 'value')
