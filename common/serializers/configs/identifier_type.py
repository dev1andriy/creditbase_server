from rest_framework import serializers
from common.models.general import IdentifierType


class IdentifierTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='IdentifierTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = IdentifierType
        fields = ('value', 'label')
