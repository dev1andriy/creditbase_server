from rest_framework import serializers
from common.models.general import DecisionMakingType


class DecisionMakingTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='DecisionMakingTypeId')

    class Meta:
        model = DecisionMakingType
        fields = ('label', 'value')
