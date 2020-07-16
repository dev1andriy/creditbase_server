from rest_framework import serializers
from common.models.general import BusinessUnit


class BusinessUnitSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='BusinessUnitId')

    class Meta:
        model = BusinessUnit
        fields = ('label', 'value')
