from rest_framework import serializers
from common.models.general import ApplicationPriority


class ApplicationPrioritySerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='ApplicationPriorityId')

    class Meta:
        model = ApplicationPriority
        fields = ('label', 'value')
