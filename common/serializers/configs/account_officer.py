from rest_framework import serializers
from common.models.general import AccountOfficer


class AccountOfficerSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='AccountOfficerId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = AccountOfficer
        fields = ('value', 'label')
