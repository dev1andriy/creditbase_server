from rest_framework import serializers
from common.models.base_party import BaseParty


class BasePartyConfigSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='BasePartyName')
    value = serializers.StringRelatedField(source='BasePartyId')

    class Meta:
        model = BaseParty
        fields = ('label', 'value')
