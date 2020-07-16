from rest_framework import serializers
from common.models.general import AlertSource


class AlertSourceSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='AlertSourceId')

    class Meta:
        model = AlertSource
        fields = ('label', 'value')
