from rest_framework import serializers
from common.models.general import AlertSeverity


class AlertSeveritySerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='AlertSeverityId')

    class Meta:
        model = AlertSeverity
        fields = ('label', 'value')
