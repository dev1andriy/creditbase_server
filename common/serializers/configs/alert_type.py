from rest_framework import serializers
from common.models.general import AlertType


class AlertTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='AlertTypeId')

    class Meta:
        model = AlertType
        fields = ('label', 'value')
