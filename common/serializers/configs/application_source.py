from rest_framework import serializers
from common.models.general import ApplicationSource


class ApplicationSourceSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='ApplicationSourceId')

    class Meta:
        model = ApplicationSource
        fields = ('label', 'value')
