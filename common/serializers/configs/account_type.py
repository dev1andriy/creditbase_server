from rest_framework import serializers
from common.models.general import AccountType


class AccountTypeSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='AccountTypeId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = AccountType
        fields = ('value', 'label')
