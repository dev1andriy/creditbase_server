from rest_framework import serializers
from common.models.document import Document


class DocumentsListSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='FileName')
    value = serializers.StringRelatedField(source='DocumentId')
    size = serializers.StringRelatedField(source='FileSize')
    type = serializers.StringRelatedField(source='FileType')

    class Meta:
        model = Document
        fields = ('label', 'value', 'size', 'type')


