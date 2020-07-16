from rest_framework import serializers
from common.models.general import AddressType


class AddressTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='AddressTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = AddressType
        fields = ('value', 'label')
