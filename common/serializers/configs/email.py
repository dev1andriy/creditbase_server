from rest_framework import serializers
from common.models.base_party import BasePartyEmail


class EmailSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='EmailFinal')
    value = serializers.StringRelatedField(source='BasePartyEmailId')

    class Meta:
        model = BasePartyEmail
        fields = ('label', 'value')
