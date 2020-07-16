from rest_framework import serializers
from common.models.general import Currency


class CurrencyListSerializer(serializers.ModelSerializer):
    id = serializers.StringRelatedField(source='CurrencyId')
    title = serializers.StringRelatedField(source='Description')

    class Meta:
        model = Currency
        fields = ('id', 'title')
