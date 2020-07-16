from rest_framework import serializers
from common.models.general import BasePartyType


class BasePartyTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='BasePartyTypeId')

    class Meta:
        model = BasePartyType
        fields = ('label', 'value')
