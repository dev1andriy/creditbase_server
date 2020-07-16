from rest_framework import serializers
from common.models.general import BuyerPower


class BuyerPowerSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='BuyerPowerId')

    class Meta:
        model = BuyerPower
        fields = ('label', 'value')
