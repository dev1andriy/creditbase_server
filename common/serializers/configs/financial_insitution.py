from rest_framework import serializers
from common.models.general import FinancialInstitution


class FinancialInstitutionSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='FinancialInstitutionId')

    class Meta:
        model = FinancialInstitution
        fields = ('label', 'value')




