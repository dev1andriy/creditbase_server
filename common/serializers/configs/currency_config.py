from rest_framework import serializers
from common.models.general import Currency


class CurrencyConfigSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='CurrencyId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = Currency
        fields = ('value', 'label')
