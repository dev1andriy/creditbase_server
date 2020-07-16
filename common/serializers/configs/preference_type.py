from rest_framework import serializers
from common.models.general import PreferenceType


class PreferenceTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='PreferenceTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = PreferenceType
        fields = ('value', 'label')
