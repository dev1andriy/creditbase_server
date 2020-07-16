from rest_framework import serializers
from common.models.base_party import BasePartyAddress


class AddressSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='AddressFinal')
    value = serializers.StringRelatedField(source='BasePartyAddressId')

    class Meta:
        model = BasePartyAddress
        fields = ('label', 'value')
