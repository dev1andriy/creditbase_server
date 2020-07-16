from rest_framework import serializers
from common.models.general import AlertSubType


class AlertSubTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='AlertSubTypeId')

    class Meta:
        model = AlertSubType
        fields = ('label', 'value')
