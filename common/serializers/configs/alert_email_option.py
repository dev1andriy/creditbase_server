from rest_framework import serializers
from common.models.general import AlertEmailOption


class AlertEmailOptionSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='AlertEmailOptionId')

    class Meta:
        model = AlertEmailOption
        fields = ('label', 'value')
