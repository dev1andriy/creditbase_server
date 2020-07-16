from rest_framework import serializers
from common.models.general import OperationalStatus


class OperationalStatusSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='OperationalStatusId')

    class Meta:
        model = OperationalStatus
        fields = ('label', 'value')
