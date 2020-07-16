from rest_framework import serializers
from common.models.general import DocumentType


class DocumentTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='DocumentTypeId')

    class Meta:
        model = DocumentType
        fields = ('label', 'value')
