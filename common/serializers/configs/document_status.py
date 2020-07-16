from rest_framework import serializers
from common.models.general import DocumentStatus


class DocumentStatusSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='DocumentStatusId')

    class Meta:
        model = DocumentStatus
        fields = ('label', 'value')
