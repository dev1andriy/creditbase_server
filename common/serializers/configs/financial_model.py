from rest_framework import serializers
from common.models.general import FinancialModel


class FinancialModelSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='FinancialModelId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = FinancialModel
        fields = ('value', 'label')
