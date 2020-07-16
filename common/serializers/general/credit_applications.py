from rest_framework import serializers
from common.models.credit_application.general import CreditApplication


class CreditApplicationsListSerializer(serializers.ModelSerializer):
    id = serializers.StringRelatedField(source='CreditApplicationId')
    title = serializers.StringRelatedField(source='CreditApplicationId')

    class Meta:
        model = CreditApplication
        fields = ('id', 'title')
