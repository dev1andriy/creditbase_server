from rest_framework import serializers
from common.models.general import AccountCategory


class AccountCategorySerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='AccountCategoryId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = AccountCategory
        fields = ('value', 'label')
