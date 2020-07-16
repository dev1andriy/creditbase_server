from rest_framework import serializers
from common.models.general import CRMStrategy


class CRMStrategySerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='CRMStrategyId')

    class Meta:
        model = CRMStrategy
        fields = ('label', 'value')
