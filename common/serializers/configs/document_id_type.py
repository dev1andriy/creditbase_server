from rest_framework import serializers
from common.models.general import DocumentIdType


class DocumentIdTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='DocumentIdTypeId')

    class Meta:
        model = DocumentIdType
        fields = ('label', 'value')
