from rest_framework import serializers
from common.models.base_party import BasePartyTelephone


class TelephoneSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='TelFormattedFinal')
    value = serializers.StringRelatedField(source='BasePartyTelephoneId')

    class Meta:
        model = BasePartyTelephone
        fields = ('label', 'value')
