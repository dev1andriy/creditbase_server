from rest_framework import serializers
from common.models.general import ApplicationType


class ApplicationTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='ApplicationTypeId')

    class Meta:
        model = ApplicationType
        fields = ('label', 'value')
