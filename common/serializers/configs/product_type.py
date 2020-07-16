from rest_framework import serializers
from common.models.general import ProductType


class ProductTypeSerializer(serializers.ModelSerializer):
    label = serializers.StringRelatedField(source='Description')
    value = serializers.StringRelatedField(source='ProductTypeId')

    class Meta:
        model = ProductType
        fields = ('label', 'value')
