from rest_framework import serializers
from common.models.general import DeclineReason


class DeclineReasonSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='DeclineReasonId')

    class Meta:
        model = DeclineReason
        fields = ('label', 'value')
