from rest_framework import serializers
from common.models.general import ProfileType


class ProfileTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='ProfileTypeId')

    class Meta:
        model = ProfileType
        fields = ('label', 'value')
