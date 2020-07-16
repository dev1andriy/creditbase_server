from rest_framework import serializers
from common.models.general import AccountClass


class AccountClassSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='AccountClassId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = AccountClass
        fields = ('value', 'label')
