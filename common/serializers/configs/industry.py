from rest_framework import serializers
from common.models.general import Industry


class IndustrySerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='IndustryId')

    class Meta:
        model = Industry
        fields = ('label', 'value')
