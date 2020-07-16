from rest_framework import serializers
from common.models.general import ApplicationStatus


class ApplicationStatusSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='ApplicationStatusId')

    class Meta:
        model = ApplicationStatus
        fields = ('label', 'value')
