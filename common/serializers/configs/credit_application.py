from rest_framework import serializers
from common.models.credit_application.general import CreditApplication


class CreditApplicationConfigSerializer(serializers.ModelSerializer):
    value = serializers.StringRelatedField(source='CreditApplicationId')
    label = serializers.StringRelatedField(source='CreditApplicationId')

    class Meta:
        model = CreditApplication
        fields = ('value', 'label')
