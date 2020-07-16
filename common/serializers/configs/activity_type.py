from rest_framework import serializers
from common.models.general import ActivityType


class ActivityTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='ActivityTypeId')

    class Meta:
        model = ActivityType
        fields = ('label', 'value')
