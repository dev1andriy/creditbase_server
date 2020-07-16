from rest_framework import serializers
from common.models.general import DecisionType


class DecisionTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='DecisionTypeId')

    class Meta:
        model = DecisionType
        fields = ('label', 'value')
