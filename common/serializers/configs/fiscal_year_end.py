from rest_framework import serializers
from common.models.general import FiscalYearEnd


class FiscalYearEndSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='FiscalYearEndId')
    label = serializers.StringRelatedField(source='Description')

    class Meta:
        model = FiscalYearEnd
        fields = ('value', 'label')
