from rest_framework import serializers
from common.models.general import AccountStatus


class AccountStatusSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='AccountStatusId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = AccountStatus
        fields = ('value', 'label')
