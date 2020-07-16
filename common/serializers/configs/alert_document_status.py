from rest_framework import serializers
from common.models.general import AlertDocumentStatus


class AlertDocumentStatusSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='AlertDocumentStatusId')

    class Meta:
        model = AlertDocumentStatus
        fields = ('label', 'value')
