from rest_framework import serializers
from common.models.general import TelephoneType


class TelephoneTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='TelephoneTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = TelephoneType
        fields = ('value', 'label')
